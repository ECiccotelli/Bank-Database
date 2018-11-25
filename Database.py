import mysql.connector
from mysql.connector import Error


def elogin():
    #Employee login
    print("---Employee login---")
    e_user = input("Please enter your username: ")
    e_pass = input("Please enter your password: ")
    # Make query to verify or reject customer login

def clogin():
    #Customer login
    print("---Customer login---")
    c_user = input("Please enter your username: ")
    c_pass = input("Please enter your password: ")
    # Make query to verify or reject employee login




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
        clogin()


    else:
        #show employee menu
        elogin()


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
    print('Connected to MySQL database')


# Creates database
#mycursor.execute("create database bank")
# Uses database
mycursor.execute("use bank")


main()
