def elogin(mycursor):
    #Employee login
    print("---Employee login---")
    e_user = input("Please enter your username: ")
    e_pass = input("Please enter your password: ")
    # Make query to verify or reject customer login

    query = "select username, password from employee_login where username = '" + e_user + "' and password = '" + e_pass + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()

    if not data:
        loggedIn = False
    else:
        print("Successfully logged in as an employee")
        loggedIn = True

    while(not loggedIn):
        print("Incorrect username or password. Try again: ")
        e_user = input("Please enter your username: ")
        e_pass = input("Please enter your password: ")
        # Make query to verify or reject customer login

        query = "select username, password from employee_login where username = '" + e_user + "' and password = '" + e_pass + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()

        if data:
            print("Successfully logged in now as an employee!")
            loggedIn = True


    #Show menu of actions


def eMenu(mycursor, conn):
    #If they have an employee login, they have to be an employee

    print("Welcome to the employee menu. Please select an option below:")
    print("1. Create new user login")
    print("2. Delete user login")
    print("3. Create new bank account")
    print("4. Create new debit card")
    print("5. View loans for your branch")
    print("6. View transaction log for all accounts")
    print("7. Exit")
    userChoice = int(input("Please make a selection: "))

    while(userChoice > 7 or userChoice < 1):
        userChoice = int(input("Incorrect option. Please select again: "))

    while userChoice != 7:
        if userChoice == 1:
            print("Create new user login option")
        elif userChoice == 2:
            print("Delete user login option")
        elif userChoice == 3:
            print("Create new bank account option")
        elif userChoice == 4:
            print("Create new debit card function")
        elif userChoice == 5:
            print("View loans option")
        elif userChoice == 6:
            print("View transaction log for all accounts option")

        #Reprompt
        print("If you would like to perform another operation, please select an option below:")
        print("1. Create new user login")
        print("2. Delete user login")
        print("3. Create new bank account")
        print("4. Create new debit card")
        print("5. View loans for your branch")
        print("6. View transaction log for all accounts")
        print("7. Exit")
        userChoice = int(input("Please make a selection: "))
    print("Exiting program. Thank you for your service, employee!")
    quit()