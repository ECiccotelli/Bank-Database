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


