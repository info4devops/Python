# connect to MYSQL Database

print(':::::::Using-pymysql:::::::)')
import pymysql

# Establish a connection to the MySQL database
con = pymysql.connect(host='localhost', database='vamsidb', user='root', password='root')
    
# Check if the connection is successful
if con is not None:
  print('Connected Successfully')
print()  


print(':::::::Using-mysql.connector:::::::)')
import mysql.connector

# Establish a connection to the MySQL database
con = mysql.connector.connect(host='localhost', database='vamsidb', user='root', password='root')
    
# Check if the connection is successful
if con is not None:
  print('Connected Successfully')