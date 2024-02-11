# Create Table in MYSQL

import pymysql
#import mysql.connector

con=pymysql.connect(host='localhost',database='vamsidb',user='root',password='root')
#con=mysql.connector.connect(host='localhost',database='vamsidb',user='root',password='root')

cursor=con.cursor()
cursor.execute('Create table students(sno int(5),sname varchar(12),sfee double(10,2),sddr varchar(12))')
print('Table Inserted Successfully')

cursor.close()
con.close()
