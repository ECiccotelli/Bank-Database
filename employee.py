'''
EMPLOYEE.PY FILE
EMPLOYEE MENU AND OPERATION FUNCTIONS
AUTHOR: ERIC CICCOTELLI
DATE: 12/6/2018
'''



import datetime
def elogin(mycursor):
    #Employee login
    print("---Employee login---")
    e_user = input("Please enter your username: ")
    e_pass = input("Please enter your password: ")
    # Make query to verify or reject customer login

    query = "select username, password from employee_login where username = '" + e_user + "' and password = '" + e_pass + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()

    #Checking results of query
    if not data:
        loggedIn = False
    else:
        print("Successfully logged in as an employee")
        loggedIn = True

    #Login failure, retry login
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
            print('\n')
            loggedIn = True




def eMenu(mycursor, conn):
    #If they have an employee login, they have to be an employee
    print("Welcome to the employee menu. Please select an option below:")
    print("1. Create new customer information")
    print("2. Create new user login")
    print("3. Delete user login")
    print("4. Create new bank account")
    print("5. Create new debit card")
    print("6. View names and balances of customers for your branch")#not done
    print("7. View transaction log for all accounts")#not done
    print("8. Exit")
    userChoice = int(input("Please make a selection: "))

    exitNumber = 8
    #Verifying user choice
    while(userChoice > exitNumber or userChoice < 1):
        userChoice = int(input("Incorrect option. Please select again: "))

    #Selecting appropriate function based on user input
    while userChoice != 8:
        if userChoice == 1:
            newCustomer(mycursor, conn)
        elif userChoice == 2:
            print("---Welcome to the new user login panel!---")
            newLogin(mycursor, conn, )
        elif userChoice == 3:
            print("---Welcome to the delete user login panel!---")
            deleteLogin(mycursor, conn)
        elif userChoice == 4:
            print("---Welcome to the new bank account panel!---")
            newBankAcct(mycursor, conn)
        elif userChoice == 5:
            print("---Welcome to the new debit card panel!---")
            newCard(mycursor, conn)
        elif userChoice == 6:
            print("---Welcome to the view customer names and balances per branch panel!---")
            viewBal(mycursor, conn)
        elif userChoice == 7:
            print("---Welcome to the view transaction log panel!---")
            viewLog(mycursor, conn)

        print('\n')
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
    #Prompt user for new information
    new_cid = input("Please enter new C_ID: ")
    new_name = input("Please enter new name: ")
    new_street = input("Please enter street: ")
    new_city = input("Please enter city: ")
    new_state = input("Please enter state: ")
    new_zip = input("Please enter zip: ")
    branch = input("Please enter associated branch: ")

    length = len(new_cid)

    #Verifying input of C_ID
    while length < 0 or not new_cid.isnumeric() or int(new_cid) < 0:
        new_cid = input("Invalid C_ID. Please enter a new C_ID: ")
        length = len(new_cid)


    #Inserting new data
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

    #Asking for confirmation for adding new login
    choice = input("Would you like to proceed? (Y/N): ")
    if choice == 'n' or choice == 'N':
        return
    #reprompt
    while choice != 'y' or choice != 'Y':
        choice = input("Invalid choice. Would you like to proceed? (Y/N): ")


    #User prompt
    c_id = input("Please enter the customer ID for new login: ")
    c_user = input("Please enter username for new login: ")
    c_pass = input("Please enter password for new login: ")

    #check c_id query
    query = "select c_id from customer where c_id = " + c_id + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()

    #Verifying input
    while not data:
        print("Error: customer ID not found! Please enter new information: ")
        c_id = input("Please enter the customer ID for new login: ")
        c_user = input("Please enter username for new login: ")
        c_pass = input("Please enter password for new login: ")
        # check c_id query
        query = "select c_id from customer where c_id = " + c_id + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()


    #Insert statement to add login values
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

    #Sending query and error catching
    try:
        query = "select c_id from customer_login where c_id = " + str(c_id) + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()
    except:
        print("Error finding C_ID. Please enter a new one from the following menu. ")

    while not data:
        c_id = input("C ID not found. Please enter another one: ")
        query = "select c_id from customer_login where c_id = " + str(c_id) + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()


    #Deleting login info and error catching
    try:
        delete = "delete from customer_login where c_id = " + c_id + ";"
        mycursor.execute(delete)
        conn.commit()
    except:
        print("Error deleting data. Please try again by selecting it from the menu.")
        return
    print("Successfully deleted login!")



def newBankAcct(mycursor, conn):
    #User prompts
    acc_num = input("Enter new account number: ")
    balance = 0
    c_id = input("Enter customer id for new account: ")
    now = datetime.datetime.now()
    date = now.date()

    #Verifying account number
    while len(acc_num) < 0 or not acc_num.isnumeric():
        acc_num = input("Invalid account number entered. Please try again: ")
        query = "select account_num from bank_accounts where account_num = " + acc_num + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()

    # Verifying C_ID input
    while len(c_id) < 0 or not c_id.isnumeric():
        c_id = input("Customer ID is invalid. Please try again: ")
        query = "select c_id from customer where c_id = " + c_id + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()



    #Checking if account number is already use
    query = "select account_num from bank_accounts where account_num = " + acc_num + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()

    #Reprompt for account number
    while data:
        acc_num = input("Account number already in use. Please try again: ")
        query = "select account_num from bank_accounts where account_num = " + acc_num + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()


    #Checking if customer ID exists
    query = "select c_id from customer where c_id = " + c_id + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()

    #Reprompt for CID
    while not data :
        c_id = input("Customer ID not found. Please try again: ")
        query = "select c_id from customer where c_id = " + c_id + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()

    #Inserting new data into database
    try:
        statement = "insert into bank_accounts values (" + acc_num + ",'Debit'," + str(balance) + "," + c_id + ",'" + str(date) + "');"
        mycursor.execute(statement)
        conn.commit()
    except:
        print("Error inserting data. Please try again from the menu.")
        return
    print("Successfully added new bank account!")






#Needs fixing
def newCard(mycursor, conn):
    #User prompts
    card_num = input("Please enter a 16 digit new card number: ")
    cvv = input("Please enter the new cvv: ")
    exp_date = input("Please enter exp date (YYYY-MM-DD): ")
    account_num = input("Enter account number that will be associated with this card: ")
    now = datetime.datetime.now()
    date_created = now.date()

    length = len(card_num)

    #Check if card number is valid and not used
    query = "select card_num from cards where card_num = '" + card_num + "';"
    mycursor.execute(query)
    data = mycursor.fetchall()


    #Verifying card number and reprompt
    while data or length != 16:
        card_num = input("Card number not valid. Try again: ")
        query = "select card_num from cards where card_num = '" + card_num + "';"
        mycursor.execute(query)
        data = mycursor.fetchall()
        length = len(card_num)


    #Check if account_num is valid and MUST BE created already
    query = "select account_num from bank_accounts where account_num = " + account_num + ";"
    mycursor.execute(query)
    data = mycursor.fetchall()



    while not data or len(account_num) < 0 or not account_num.isnumeric():
        account_num = input("Account number not valid. Try again: ")
        query = "select account_num from bank_accounts where account_num = " + account_num + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()

    #Sending insert to database
    try:
        insert = "insert into cards values ('" + card_num + "'," + cvv + ",'" + exp_date + "'," + account_num + ",'" \
                 + str(date_created) + "');"
        mycursor.execute(insert)
        conn.commit()
        print("Successfully added new card!")
    except:
        print("Error adding card. Please try again")



def viewBal(mycursor, conn):
    branch_id = input("Please enter branch id: ")

    #Verifying input
    while not branch_id.isnumeric():
        branch_id = input("Please enter a valid branch id: ")

    #Sending query
    try:
        query = "select c_id, name, balance from customer natural join bank_accounts where branch_id = " + branch_id + ";"
        #Using NATURAL JOIN to connect two tables to present to user
        mycursor.execute(query)
        data = mycursor.fetchall()
    except:
        print("Error querying database")

    #Processing data from database
    if not data:
        print("No customers found in entered branch id: " + branch_id)
    else:
        print("Here are the IDS, Names and Balances for every customer at branch: " + branch_id)
        for row in data:
            print("ID: " + str(row[0]) + "  Name: " + str(row[1]) + "  Balance: $" + str(row[2]))




def viewLog(mycursor, conn):
    acc_num = input("Enter account number to view log for that account: ")

    #Verifying input
    while not acc_num.isnumeric():
        acc_num = input("Please enter a valid account number: ")

    #Sending query
    try:
        query = "select * from transaction_log where account_num = " + acc_num + ";"
        mycursor.execute(query)
        data = mycursor.fetchall()
    except:
        print("Error querying database")
        return

    #If no results found
    if not data:
        print("No accounts with that number exist in the database!")
        return
    #Output data from database
    for row in data:
        print("Amount: $" + str(row[0]) + "  Type: " + str(row[1]) + "  Date & Time: " + str(row[2]) +
              "  Account number: " + str(row[3]))