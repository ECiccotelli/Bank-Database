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
    print("Welcome to the customer menu. Please select an option below: ")
    print("1. Check balance of your account")
    print("2. Deposit money into your account")
    print("3. Withdraw money from your account")
    print("4. Make a loan payment")
    print("5. Exit ")
    userChoice = input("Please make a selection: ")

    while(int(userChoice) < 1 or int(userChoice) > 5):
        userChoice = input("Incorrect option. Please select again: ")

    userChoice = int(userChoice)
    if(userChoice == 1):
        #Do check balance
        print("Checking balance")
    elif (userChoice == 2):
        #Do deposit function
        print("Depositing")
    elif (userChoice == 3):
        #Withdraw function
        print("Withdraw")
    elif (userChoice == 4):
        #Make a loan payment
        print("Making a loan payment")
    else:
        print("Exiting the program. Thank you for visiting E Bank!")
        quit()

def checkBal(mycursor):
    print("Checking bal")