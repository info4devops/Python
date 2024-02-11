# Create a table and insert data inside that table in MYSQL

import pymysql

try:
    con = pymysql.connect(host='localhost', database='vamsidb', user='root', password='root')

    cursor = con.cursor()

    # Create the table with correct field names and data types
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS cricketers(sno INT(5), sname VARCHAR(12), sfee DOUBLE(10,2), saddr VARCHAR(12))')

    # Insert data into the table using parameterized query
    query = "INSERT INTO cricketers(sno, sname, sfee, saddr) VALUES (%s, %s, %s, %s)"
    records = [(100, 'rohit', 1000, 'Mumbai'),
               (101, 'Virat', 2000, 'Blr'),
               (102, 'Gill', 3000, 'Pune'),
               (103, 'Surya', 4500, 'Hyd')]
    cursor.executemany(query, records)

    # Commit the transaction
    con.commit()
    print('Records Inserted Successfully')

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem with SQL:', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
