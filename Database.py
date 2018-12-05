'''
DATABASE.PY FILE
MAIN DRIVER FUNCTION AND FILE
AUTHOR: ERIC CICCOTELLI
DATE: 12/6/2018
'''


import mysql.connector
from mysql.connector import Error
from insertScript import insertTables, insertbranch, insertCustomer, insertEmployee, insertOther
from customer import clogin, cMenu
from employee import elogin, eMenu



def main():
    # main driver function

    customer = False
    userInput = input("Are you an employee or a customer? (E/C): ")

    #Check if user is customer or employee
    while (userInput != "E" and userInput != "C" and userInput != "e" and userInput != "c"):
        userInput = input("Incorrect option. Please enter again (E/C): ")

    if userInput == 'C' or userInput == 'c':
        customer = True

    #Call customer logjn, menu if user is a customer
    if(customer):
        #show customer menu
        clogin(mycursor)
        #Customer menu here
        cMenu(mycursor, conn)

    #Otherwise, call login and menu for employee
    else:
        elogin(mycursor)
        #Employee menu here
        eMenu(mycursor, conn)


    conn.close()





# Connects to MySQL
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               password='root')

mycursor = conn.cursor()
if conn.is_connected():
    connected = True
else:
    print('Error connecting to database')

# Creates database
try:
    mycursor.execute("create database bank")
except:
    #This is executed if database already exists (most likely the error)
    mycursor.execute("drop database bank")
    mycursor.execute("create database bank")

# Uses database
mycursor.execute("use bank")

#Inserting data and tables into database
insertTables(mycursor, conn)
insertbranch(mycursor, conn)
insertEmployee(mycursor, conn)
insertCustomer(mycursor, conn)
insertOther(mycursor, conn)
main()
