def clogin(mycursor):
    #Customer login
    print("---Customer login---")
    c_user = input("Please enter your username: ")
    c_pass = input("Please enter your password: ")
    # Make query to verify or reject employee login

    query = "select username, password from customer_login where username = '" + c_user + "' and password = '" + c_pass + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()

    if not data:
        loggedIn = False
    else:
        print("Successfully logged in as a customer")
        loggedIn = True

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

def cMenu(mycursor, conn):
    #Customer menu
    #ENTER ACCOUNT NUMBER BEFORE MENU?

    acc_num = input("Please enter your account number: ")

    query = "select account_num from bank_accounts where account_num = '" + acc_num + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()

    while not data:
        acc_num = input("Account number not found. Try again: ")
        query = "select account_num from bank_accounts where account_num = '" + acc_num + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()

    print("Successfully found account.")
    print("Welcome to the customer menu for this account. Please select an option below: ")
    print("1. Check balance of your account")
    print("2. Deposit money into your account")
    print("3. Withdraw money from your account")
    print("4. Make a loan payment")
    print("5. Exit ")
    userChoice = input("Please make a selection: ")

    while(int(userChoice) < 1 or int(userChoice) > 5):
        userChoice = input("Incorrect option. Please select again: ")

    userChoice = int(userChoice)

    while(userChoice != 5):
        if(userChoice == 1):
            #Do check balance
            print("Checking balance")
            bal = checkBal(mycursor, acc_num)
            print("Balance is $" + str(bal) + "!")
        elif (userChoice == 2):
            #Do deposit function
            print("Depositing")
            deposit(mycursor, conn, acc_num)
        elif (userChoice == 3):
            #Withdraw function
            print("Withdraw")
            withdraw(mycursor, conn, acc_num)
        elif (userChoice == 4):
            #Make a loan payment
            print("Making a loan payment")

        #Reprompt
        print("If you would like to perform another operation, please select an option below: ")
        print("1. Check balance of your account")
        print("2. Deposit money into your account")
        print("3. Withdraw money from your account")
        print("4. Make a loan payment")
        print("5. Exit ")
        userChoice = input("Please make a selection: ")
        userChoice = int(userChoice)
    print("Exiting the program. Thank you for visiting E Bank!")
    quit()

def checkBal(mycursor, acc_num):
    print("Checking bal")
    query = "select balance from bank_accounts where account_num = '" + acc_num + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #print("Current balance is: $" + str(data[0][0]))
    return data[0][0]

def deposit(mycursor, conn, acc_num):
    amount = float(input("How much do you want to deposit? "))
    balance = checkBal(mycursor, acc_num)
    newBal = balance + amount
    update = "update bank_accounts set balance = " + str(newBal) + " where account_num = '" + acc_num + "';"
    try:
        mycursor.execute(update)
        conn.commit()
        print("Old balance was: " + str(balance))
        print("New balance is now " + str(newBal))
    except:
        print("Error depositing")

def withdraw(mycursor, conn, acc_num):
    balance = checkBal(mycursor, acc_num)
    print("Your current balance is: $" + str(balance))
    amount = float(input("How much do you want to withdraw? "))
    while float(balance) < amount:
        amount = float(input("Error: Cannot withdraw that amount. Try again: "))
    newBal = float(balance) - amount
    update = "update bank_accounts set balance = " + str(newBal) + " where account_num = '" + acc_num + "';"
    try:
        mycursor.execute(update)
        conn.commit()
        print("Old balance was: " + str(balance))
        print("New balance is now " + str(newBal))
    except:
        print("Error withdrawing money")

