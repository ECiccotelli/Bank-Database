import mysql.connector
from mysql.connector import Error

def insertbranch(mycursor, conn):

    print("Inserting branch data")

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



    conn.commit()
    print("Inserted branch data successfully")
def insertCustomer(mycursor, conn):
    print("inserting customer")





def insertEmployee(mycursor, conn):
    print("inserting employee")

    #Employee table
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
        print(query)

    #Employee logins
    #Employee phone


def insertOther(mycursor, conn):
    print("inserting other")


