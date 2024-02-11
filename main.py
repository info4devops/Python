import pymysql

try:
    # Establish a connection to the MySQL database
    con = pymysql.connect(host='localhost', database='vamsidb', user='root', password='root')
    
    # Check if the connection is successful
    if con is not None:
        print('Connected Successfully')

except pymysql.DatabaseError as e:
    # Print the error message
    print('There is a problem with the database connection:', e)

finally:
    # Close the connection object
    if con:
        con.close()
