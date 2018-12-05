import mysql.connector
from mysql.connector import Error

def insertTables(mycursor, conn):
    #Insert tables

    statement = "create table branch (b_id int, name varchar(32), address varchar(75), primary key (b_id));"
    mycursor.execute(statement)

    statement = "create table b_phone (b_id int, phone_num varchar(20),  primary key (b_id, phone_num), foreign key " \
                "(b_id) references branch (b_id));"
    mycursor.execute(statement)

    statement = "create table employee(e_id int,name varchar(50),street varchar(50),city varchar(35)," \
                "state varchar(5),zip varchar(5),branch_id int, primary key (e_id),foreign key (branch_id) " \
                "references branch(b_id));"

    mycursor.execute(statement)
    statement = "create table e_phone(e_id int,phone_num varchar(20), primary key(e_id, phone_num)," \
                "foreign key (e_id) references employee (e_id));"
    mycursor.execute(statement)

    statement = "create table employee_login(	e_id int,    username varchar(32),    " \
                "password varchar(16),    primary key (e_id),    foreign key (e_id) references employee (e_id));"

    mycursor.execute(statement)

    statement = "create table customer(	c_id int,    name varchar(50),    street varchar(50),    " \
                "city varchar(35),    state varchar(5),    zip varchar(5),    branch_id int,    " \
                "primary key (c_id),foreign key (branch_id) references branch (b_id));"

    mycursor.execute(statement)

    statement = "create table c_phone(	c_id int,    phone_num varchar(20),    primary key (c_id, phone_num),    " \
                "foreign key (c_id) references customer (c_id));"

    mycursor.execute(statement)

    statement = "create table customer_login(c_id int,    username varchar(32),    password varchar(16),    " \
                "primary key (c_id),    foreign key (c_id) references customer (c_id));"

    mycursor.execute(statement)

    statement = "create table bank_accounts(	account_num int,    type varchar(6),    balance double,    c_id int,  " \
                "  date_created DATE,    primary key (account_num),    foreign key (c_id) references customer (c_id));"

    mycursor.execute(statement)

    statement = "create table transaction_log(	amount double,    type varchar(10),    datetime DATETIME,    " \
                "account_num int,    primary key (account_num, datetime, type),    " \
                "foreign key (account_num) references bank_accounts (account_num));"
    mycursor.execute(statement)

    statement = "create table cards(	card_num varchar(16),    cvv int,    exp_date DATE,    " \
                "account_num int,    date_created DATE,    primary key (card_num),    " \
                "foreign key (account_num) references bank_accounts(account_num));"
    mycursor.execute(statement)


def insertbranch(mycursor, conn):
    #Branch data

    branchIds = [123, 456, 789, 173, 901, 824, 432, 768, 936, 800]
    branchNames = ['Uptown', 'Downtown', 'West', 'East', 'Scranton', 'White Plains',
                   'Packford', 'Davis', 'Financial District', 'SOHO']

    branchAddresses = ['123 Maple Street, Bronx, NY 10471', '852 Woodward Street Wilmington NC 10605',
                       '200 West Pickle Street Valhalla NY 10595', '750 East Madison Street White Plains NY 10603',
                       '555 Walnut Avenue Cheshire CT 06410','2 Harron Drive Corpus Christi TX 78476',
                       '1253 Ridenour Street Baltimore MD 21202', '3936 Vineyard Drive Westerville OH 43081',
                       '2988 Roy Alley Milwaukee WI 53202', '3277 Nancy Street San Antonio TX 78238']


    #Insert statement in loop
    for i in range(0, 10):
        #For loop to insert statements
        query = "insert into branch values (" + str(branchIds[i]) + ",'" + branchNames[i] + "','" + branchAddresses[i] + "');"
        mycursor.execute(query)
        #print("Query executed")



    # -----Branch phone numbers table-----
    b_phones = ['232-851-3903', '343-339-3434', '341-353-0099', '111-997-8563', '444-466-2364', '999-921-3575',
                '654-536-2328', '423-580-3424', '653-778-3574', '222-469-2248']
    for i in range(0, 10):
        query = "insert into b_phone values (" + str(branchIds[i]) + ",'" + b_phones[i] + "');"
        mycursor.execute(query)

    conn.commit()



def insertCustomer(mycursor, conn):
    #-----Customer table-----
    c_id = [980, 987, 876, 765, 654, 543, 432, 321, 232, 434, 111]
    c_names = ['Nora Longfellow','Vanda Mccallie','Jeremiah Randolph','Daine Lurry','Sanjuanita Thornhill',
               'Donette Buechner','Berta Danaher','Roland Rommel','Heidy Rexroat','Ebonie Santee', 'ERICCC RICH']
    c_street = ['78 Roosevelt Dr. ', '8860 Bellevue St.', '13 Clay Ave. ', '8771 South Creekside St. ',
                '893 Coffee Ave. ', '553 West Summerhouse Drive ', '878 Main St. ', '127 Miller Drive ',
                '8291 Trusel Court ', '6 Saxon Avenue ', '29 DAVIS']
    c_city = ['Horn Lake', 'Bangor', 'Franklin', 'Antioch', 'Redford', 'Cuyahoga Falls', 'Thornton', 'Wilson',
              'Olney', 'Massapequa Park', 'VALHALLA']
    c_state = ['MS ', 'ME ', 'MA ', 'TN', 'MI', 'OH ', 'CO ', 'NC ', 'MD ', 'NY ', 'NY']
    c_zip = ['38637', '04401', '02038', '37013', '48239', '44221',
             '80241', '27893', '20832', '11762', '10595']
    c_branches = [123, 456, 789, 173, 901, 824, 432, 768, 936, 800, 800]
    for i in range(0, 11):
        query = "insert into customer values (" + str(c_id[i]) + ",'" + c_names[i] + "','" + c_street[
            i] + "','" + c_city[i] + "','" + c_state[i] + "','" + c_zip[i] + "'," + str(c_branches[i]) + ");"
        mycursor.execute(query)



    #-----Customer phone-----
    c_phones = ['434-467-9513', '902-860-5881', '952-643-7583', '982-689-1640', '505-493-6170', '986-522-5543',
                '233-885-6363', '355-955-5585', '228-657-8091', '782-805-3096']
    for i in range(0, 10):
        query = "insert into c_phone values (" + str(c_id[i]) + ",'" + c_phones[i] + "');"
        mycursor.execute(query)


    #-----Customer logins-----
    c_usernames = ['ctest', 'phizntrg@live.com', 'telbij@comcast.net', 'aprakash@optonline.net', 'bolow@sbcglobal.net',
                   'joelw@comcast.net', 'bjoern@verizon.net', 'jemarch@yahoo.ca', 'murdocj@yahoo.ca', 'tattooman@sbcglobal.net']
    c_passwords = ['ctest', 'pass', 'w0rd', 'pAsS', 'pazzword', 'myPass', 'passWORD','wordpass', 'abc123',  'def456']
    for i in range(0, 10):
        query = "insert into customer_login values (" + str(c_id[i]) + ",'" + c_usernames[i] + "','" + c_passwords[i] + "');"
        mycursor.execute(query)
    conn.commit()




def insertEmployee(mycursor, conn):

    #-----Employee table-----
    e_id = [111, 222, 333, 444, 555, 666, 777, 888, 999, 000]
    e_names = ['Wilford Prokop', 'Clarine Corbo', 'Jerry Santi', 'Celeste Gadberry', 'Denice Hemphill',
               'Nettie Kimmer', 'Laura Deanda', 'Ethel Sokoloski', 'Jacquelynn Twilley', 'Jennell Lofgren']
    e_street = ['3726 Romines Mill Road', '1111 Hallow Road', '9382 Hiney Road', '3220 Jefferson Road',
                '3311 Washington Place', '1888 Harrison Street', '55 Grant Mill Road', '37 McKinley Ave',
                '39 Willis Street', '90 Adams Road']
    e_city = ['Bronx', 'Wilmington', 'Valhalla', 'White Plains', 'Cheshire', 'Corpus Christi', 'Baltimore', 'Westerville',
              'Milwaukee', 'San Antonio']
    e_state = ['NY', 'NC', 'NY', 'NY', 'CT', 'TX', 'MD', 'OH', 'WI', 'TX']
    e_zip = ['10471', '10605', '10595', '10603', '06410', '88476',
             '21202', '43081', '53202', '78238']
    e_branches = [123, 456, 789, 173, 901, 824, 432, 768, 936, 800]
    for i in range(0, 10):
        query = "insert into employee values (" + str(e_id[i]) + ",'" + e_names[i] + "','" + e_street[
            i] + "','" + e_city[i] + "','" + e_state[i] + "','" + e_zip[i] + "'," + str(e_branches[i]) + ");"
        mycursor.execute(query)


    #-----Employee phone-----
    e_phones = ['757-851-8949', '309-339-3348', '740-353-0099', '559-997-9781', '303-466-3676', '915-921-2606',
                '706-536-9714', '423-580-7706', '941-778-7688', '619-469-9102']
    for i in range(0, 10):
        query = "insert into e_phone values (" + str(e_id[i]) + ",'" + e_phones[i] + "');"
        mycursor.execute(query)


    #-----Employee logins-----
    e_usernames = ['etest', 'clarine4@gmail.com', 'jerry05@gmail.com', 'celeste032@gmail.com', 'denice1@gmail.com',
                   'nettie74@gmail.com', 'laura@gmail.com', 'ethel542@gmail.com', 'jacquelynn24@gmail.com', 'jennell23@gmail.com']
    e_passwords = ['etest', 'pAsSwOrD', 'jerryisawesome', 'celestethebest', 'denicethebeast', 'nettieYetty', 'lauraPass',
                   'ethelpassworD', 'jackieChan',  'jennellPassWord']
    for i in range(0, 10):
        query = "insert into employee_login values (" + str(e_id[i]) + ",'" + e_usernames[i] + "','" + e_passwords[i] + "');"
        mycursor.execute(query)

    conn.commit()



def insertOther(mycursor, conn):

    #-----Bank accounts table-----
    acc_num = [1001, 2001, 3001, 4001, 5001, 6001, 7001, 8001, 9001, 1101]
    #type = ['Debit', 'Debit','Debit','Debit','Debit','Debit','Debit','Debit','Debit','Debit',]
    balance = [0, 50, 624.60, 5025.50, 150.25, 100, 100, 900.27, 805.50, 2500]
    c_id = [980, 987, 876, 765, 654, 543, 432, 321, 232, 434]
    #Date in YYYY-MM-DD
    date_created = ['2018-01-01', '2017-07-07','2015-01-01','2018-12-12','2016-05-30','2016-06-03','2017-08-14',
                    '2014-02-09','2012-10-10','2013-07-07',]
    for i in range(0, 10):
        query = "insert into bank_accounts values (" + str(acc_num[i]) + ",'Debit'," + str(balance[i]) + "," + str(c_id[i]) + ",'" + date_created[i] + "');"
        mycursor.execute(query)



    #-----Transaction log table-----
    amounts = [50, 75, 100, 24.50, 75, 5, 200, 3500, 900, 250]
    type = ['Withdraw', 'Deposit','Withdraw','Deposit','Deposit','Deposit','Withdraw','Deposit','Withdraw','Deposit']

    datetimes = ['2018-01-01 05:50:55', '2017-07-07 09:20:25','2015-01-01 11:50:55','2018-12-12 03:30:30',
                 '2016-05-30 09:45:27','2016-06-03 04:00:00','2017-08-14 02:20:20',
                    '2014-02-09 10:35:43','2012-10-10 06:51:52','2013-07-07 08:51:00',]
    #acc_num defined above
    for i in range(0, 10):
        query = "insert into transaction_log values (" + str(amounts[i]) + ",'" + type[i] + "','" + datetimes[i] + "'," + str(acc_num[i]) + ");"
        mycursor.execute(query)


    #-----Cards table-----

    card_nums = ['1111222233334444', '2222333344445555', '3333444455556666', '4444555566667777', '5555666677778888',
                 '6666777788889999', '7777888899990000', '8888999900001111', '9999000011112222', '0000111122223333']
    cvv = ['123', '456', '789', '908', '809', '706', '302', '504', '201','482']
    exp_date =  ['2020-01-01', '2020-07-07','2021-01-01','2022-12-12','2023-05-30','2024-06-03','2022-08-14',
                    '2019-02-09','2020-10-10','2019-07-07',]
    #account numbers defined above acc_num
    #date created defined above date_created
    for i in range(0, 10):
        query = "insert into cards values ('" + card_nums[i] + "','" + cvv[i] + "','" + exp_date[i] + "'," + str(acc_num[i]) + ",'" + date_created[i] + "');"
        mycursor.execute(query)


    conn.commit()