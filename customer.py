'''
CUSTOMER.PY FILE
CUSTOMER MENU AND OPERATION FUNCTIONS
AUTHOR: ERIC CICCOTELLI
DATE: 12/6/2018
'''


import datetime
#CUSTOMER LOGIN
def clogin(mycursor):
    #Customer login
    print("---Customer login---")
    c_user = input("Please enter your username: ")
    c_pass = input("Please enter your password: ")


    # Make query to verify or reject employee login
    try:
        query = "select username, password from customer_login where username = '" + c_user + "' and password = '" + c_pass + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()
    except:
        print("Error logging in. Please try again.")


    if not data:
        loggedIn = False
    else:
        print("Successfully logged in as a customer")
        print('\n')
        loggedIn = True

    #If login not successful
    while (not loggedIn):
        print("Incorrect username or password. Try again: ")
        c_user = input("Please enter your username: ")
        c_pass = input("Please enter your password: ")
        # Make query to verify or reject customer login

        query = "select username, password from customer_login where username = '" + c_user + "' and password = '" + c_pass + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()

        if data:
            print("Successfully logged in now as a customer!")
            loggedIn = True


#CUSTOMER MENU
def cMenu(mycursor, conn):
    #Customer menu

    acc_num = input("Please enter your account number: ")

    try:
        query = "select account_num from bank_accounts where account_num = '" + acc_num + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()
    except:
        print("Error verifying account number. Please try again.")

    while not data:
        acc_num = input("Account number not found. Please enter a different one: ")
        query = "select account_num from bank_accounts where account_num = '" + acc_num + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()

    #Initial menu
    print("Successfully found account.")
    print("Welcome to the customer menu for this account. Please select an option below: ")
    print("1. Check balance of your account")
    print("2. Deposit money into your account")
    print("3. Withdraw money from your account")
    print("4. Exit ")
    userChoice = input("Please make a selection: ")

    while(int(userChoice) < 1 or int(userChoice) > 4):
        userChoice = input("Incorrect option. Please select again: ")

    userChoice = int(userChoice)

    while(userChoice != 4):
        if(userChoice == 1):
            #Do check balance
            print("Checking balance...")
            bal = checkBal(mycursor, acc_num)
            print("Balance is $" + str(bal) + "!")
        elif (userChoice == 2):
            #Do deposit function
            print("---Welcome to the deposit operation!---")
            deposit(mycursor, conn, acc_num)
        elif (userChoice == 3):
            #Withdraw function
            print("---Welcome to the withdraw operation!---")
            withdraw(mycursor, conn, acc_num)

        print('\n')
        #Reprompt
        print("If you would like to perform another operation, please select an option below: ")
        print("1. Check balance of your account")
        print("2. Deposit money into your account")
        print("3. Withdraw money from your account")
        print("4. Exit ")
        userChoice = input("Please make a selection: ")
        userChoice = int(userChoice)

        while (int(userChoice) < 1 or int(userChoice) > 4):
            userChoice = input("Incorrect option. Please select again: ")

    #Exits when 4 is entered
    print("Exiting the program. Thank you for visiting EricBank!")
    quit()



#CHECK BALANCE
def checkBal(mycursor, acc_num):
    query = "select balance from bank_accounts where account_num = '" + acc_num + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #print("Current balance is: $" + str(data[0][0]))
    return data[0][0]




#DEPOSIT INTO ACCOUNT
def deposit(mycursor, conn, acc_num):
    amount = float(input("How much do you want to deposit? "))
    balance = checkBal(mycursor, acc_num)

    #Verify user input
    while amount < 0:
        amount = float(input("Please enter a positive number to deposit: "))

    newBal = balance + amount

    #Make update request, output old and new balances
    update = "update bank_accounts set balance = " + str(newBal) + " where account_num = '" + acc_num + "';"
    try:
        mycursor.execute(update)
        conn.commit()
        print("Old balance was: $" + str(balance))
        print("New balance is now $" + str(newBal))
    except:
        print("Error depositing")


    now = datetime.datetime.now()
    # Adding transaction to transaction log
    insert = "insert into transaction_log values(" + str(amount) + ",'Deposit','" + str(now) + "'," + str(acc_num) + ");"
    try:
        mycursor.execute(insert)
        conn.commit()
    except:
        print("Error adding transaction to transaction log")




#WITHDRAW FROM ACCOUNT
def withdraw(mycursor, conn, acc_num):
    #User input
    balance = checkBal(mycursor, acc_num)
    print("Your current balance is: $" + str(balance))
    amount = float(input("How much do you want to withdraw? "))

    #Verifying user input
    while float(balance) < amount or amount < 0:
        amount = float(input("Error: Cannot withdraw that amount. Try again: "))

    #Send update to database, output new and old balances
    newBal = float(balance) - amount
    update = "update bank_accounts set balance = " + str(newBal) + " where account_num = '" + acc_num + "';"
    try:
        mycursor.execute(update)
        conn.commit()
        print("Old balance was: $" + str(balance))
        print("New balance is now $" + str(newBal))
    except:
        print("Error withdrawing money")


    now = datetime.datetime.now()
    #Adding transaction to transaction log
    insert = "insert into transaction_log values(" + str(amount) + ",'Withdraw','" + str(now) + "'," + str(acc_num) + ");"
    try:
        mycursor.execute(insert)
        conn.commit()
    except:
        print("Error adding transaction to transaction log")

