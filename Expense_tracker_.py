import sqlite3
import datetime

class Mymain:

# Defining the main function to operate other function in the body
 def main(self):
        while (True):
            print("=====================================================")
            print(" -=-=-| Welcome to the Expense Tracker system |-=-=-   ")
            print("=====================================================")
            print("Enter 1. To enter expenses into your database")
            print("Enter 2. To view current expenses with date")
            print("Enter 3. To see total spending")
            print("Enter 4. To exit")
            print("=====================================================")
            try:
                self.a = int(input("Select a choice (1-4): "))
                print()
                if (self.a == 1):
                    d = Data_input()     # creating a Data_input class object
                    d.data()             # calling data() function with the  Data_input class object

                elif (self.a == 2):
                    v = Data_input()     # creating a Data_input class object
                    v.view_data()        # calling view_data() function with the  Data_input class object

                elif (self.a == 3):
                    t = Data_input()     # creating a Data_input class object
                    t.total_amount()     # calling total_amount() function with the  Data_input class object

                elif (self.a == 4):
                    print("Thank you for using Expense Tracker system.")
                    break
                else:
                    print("Please enter a valid choice from 1-4")
            except ValueError:                                    # Exception-handling
                print("Oops ! Please input as suggested.")


class Data_input:

  # Function for entering data into database

  def data(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()

        # creating the Expense table in the database
        cursor.execute('''
        create table if not exists expense(
                   item string, 
                   price number, 
                   date string )
        ''')

        # Getting user input for the expense data
        i_item = str(input('Enter the item you purchased:'))
        i_price = float(input('Cost of item in Dollars:'))
        date_entry = input('Enter a purchase date in YYYY/MM/DD format:')
        year, month, day = map(int, date_entry.split('/'))
        i_date = datetime.date(year, month, day)

        # sql query to enter data into the database
        cursor.execute("""
                INSERT INTO expense(item, price, date)
                VALUES (?,?,?)
        """, (i_item, i_price, i_date))
        conn.commit()
        print('Data entered successfully.')

  # Function for viewing expense data from database

  def view_data(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()

        # Sql query to get all the stored data in database
        cursor.execute(""" SELECT * from expense
        """)
        rows = cursor.fetchall()   # Fetching all the entries from the database based on query
        print ('*** Every Expense data you entered with date ***')
        print()
        for r in rows:
            print("Item-Name:", r[0], "|", "Price:", '$', r[1], "|", "Date:", r[2])
            print("--------------------------------------------------------------------")

  # Function for viewing total expense so far

  def total_amount(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT sum(price) from expense
        """)
        total = cursor.fetchone()  # Fetching only one output which is the total amount
        for row in total:
            print("Total Spending in Dollars:", "$", row)


# Calling the main Function

m = Mymain()
m.main()
