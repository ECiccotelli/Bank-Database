import mysql.connector
from mysql.connector import Error
from insertScript import insertTables, insertbranch, insertCustomer, insertEmployee, insertOther
from customer import clogin, cMenu
from employee import elogin, eMenu



def main():
    # main function

    customer = False

    userInput = input("Are you an employee or a customer? (E/C): ")


    while (userInput != "E" and userInput != "C" and userInput != "e" and userInput != "c"):
        userInput = input("Incorrect option. Please enter again (E/C): ")

    if userInput == 'C' or userInput == 'c':
        customer = True


    if(customer):
        #show customer menu
        clogin(mycursor)
        #Customer menu here
        cMenu(mycursor, conn)


    else:
        elogin(mycursor)
        #Employee menu here
        eMenu(mycursor, conn)



    #Creates table
    #mycursor.execute("create table department(dname varchar(20), location varchar(3),budget int, primary key(dname));")
    #conn.commit()



    conn.close()


# Connects to MySQL
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               password='root')

mycursor = conn.cursor()
if conn.is_connected():
    connected = True
    #print('Connected to MySQL database')
else:
    print('Error connecting to database')

# Creates database
try:
    mycursor.execute("create database bank")
except:
    #print("Database already exists! Taking care of that now...")
    mycursor.execute("drop database bank")
    mycursor.execute("create database bank")

# Uses database
mycursor.execute("use bank")

insertTables(mycursor, conn)
insertbranch(mycursor, conn)
insertEmployee(mycursor, conn)
insertCustomer(mycursor, conn)
insertOther(mycursor, conn)
main()
