# Insert data using dynamic input

import cx_Oracle

try:
    #con = cx_Oracle.connect('scott/tiger@localhost/orcl')
    con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
    cursor = con.cursor()
    while True:
        Sno = int(input('Enter Student Number:'))
        Sname = input('Enter Student name:')
        Sfee = int(input('Enter Student Fee:'))
        query = f"Insert into student values({Sno},'{Sname}',{Sfee})"
        cursor.execute(query)
        print('Records Inserted succesfully')
        option = input('Do You want to enter another student details[Yes/No]:')
        if option in ['Yes', 'YES', 'y', 'Y']:
            continue
        else:
            con.commit()
            break

except cx_Oracle.DataError as e:
    if con:
        con.rollback()
        print('There is a problem with sql:', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
