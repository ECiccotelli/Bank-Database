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
    print("1. Create new customer information")
    print("2. Create new user login")
    print("3. Delete user login")
    print("4. Create new bank account")
    print("5. Create new debit card")
    print("6. View loans for your branch")
    print("7. View transaction log for all accounts")
    print("8. Exit")
    userChoice = int(input("Please make a selection: "))

    exitNumber = 8
    while(userChoice > exitNumber or userChoice < 1):
        userChoice = int(input("Incorrect option. Please select again: "))

    while userChoice != 8:
        if userChoice == 1:
            newCustomer(mycursor, conn)
        elif userChoice == 2:
            print("Create new user login option")
            newLogin(mycursor, conn, )
        elif userChoice == 3:
            print("Delete user login option")
            deleteLogin(mycursor, conn)
        elif userChoice == 4:
            print("Create new bank account option")
        elif userChoice == 5:
            print("Create new debit card function")
        elif userChoice == 6:
            print("View customer names and balances per branch")
        elif userChoice == 7:
            print("View transaction log for all accounts option")

        #Reprompt
        print("If you would like to perform another operation, please select an option below:")
        print("1. Create new customer information")
        print("2. Create new user login")
        print("3. Delete user login")
        print("4. Create new bank account")
        print("5. Create new debit card")
        print("6. See all customer names and balances per branch")
        print("7. View transaction log for all accounts")
        print(str(exitNumber) + ". Exit")
        userChoice = int(input("Please make a selection: "))
    print("Exiting program. Thank you for your work, employee!")
    quit()


def newCustomer(mycursor, conn):
    print("New customer!")
    new_cid = input("Please enter new C_ID: ")
    new_name = input("Please enter new name: ")
    new_street = input("Please enter street: ")
    new_city = input("Please enter city: ")
    new_state = input("Please enter state: ")
    new_zip = input("Please enter zip: ")
    branch = input("Please enter associated branch: ")

    try:
        query = "insert into customer values (" + str(new_cid) + ",'" + new_name + "','" + new_street + "','" + new_city + \
            "','" + new_state + "','" + new_zip + "'," + str(branch) + ");"
        mycursor.execute(query)
        conn.commit()
    except:
        print("Error inserting information. This could be because the customer ID already exists or the branch ID "
              "does not exist. Please try again from the menu!")
        return

    print("Added new customer information successfully!")


def newLogin(mycursor, conn, ):
    print("Warning: You must create a new customer ID before proceeding. If this customer already has a login, you may"
          "not create another!")

    c_id = input("Please enter the customer ID for new login: ")
    c_user = input("Please enter username for new login: ")
    c_pass = input("Please enter password for new login: ")

    #check c_id query
    query = "select c_id from customer where c_id = " + c_id + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()

    while not data:
        print("Error: customer ID not found! Please enter new information: ")
        c_id = input("Please enter the customer ID for new login: ")
        c_user = input("Please enter username for new login: ")
        c_pass = input("Please enter password for new login: ")
        # check c_id query
        query = "select c_id from customer where c_id = " + c_id + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()

    #If customer ID is found
    #Query to check if user already has a login

    query = "insert into customer_login values ("+ str(c_id) + ",'" + c_user + "','" + c_pass + "');"
    try:
        mycursor.execute(query)
        conn.commit()
    except:
        print("Error adding values! This may be caused by the customer ID already being associated with a login. Please try"
              "again from the menu! ")
        return
    print("Added new customer login successfully!")


def deleteLogin(mycursor, conn):
    c_id = input("Please enter customer id of login that you want to delete: ")

    query = "select c_id from customer_login where c_id = " + str(c_id) + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()

    while not data:
        c_id = input("C ID not found. Please enter another one: ")
        query = "select c_id from customer_login where c_id = " + str(c_id) + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()

    try:
        delete = "delete from customer_login where c_id = " + c_id + ";"
        mycursor.execute(delete)
        conn.commit()
    except:
        print("Error deleting data. Please try again by selecting it from the menu.")
        return
    print("Successfully deleted login!")
#print("4. Create new bank account")
#print("5. Create new debit card")
#print("6. See all customer names and balances per branch")
#print("7. View transaction log for all accounts")