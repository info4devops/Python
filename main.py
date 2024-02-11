import cx_Oracle
try:
    #con=cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
    con=cx_Oracle.connect('scott/tiger@localhost/orcl')

    cursor=con.cursor()
    cursor.execute("Insert into employees values (11,'sunny',121212,'BLR')")
    con.commit()
    print('Records inserted successfully')
except cx_Oracle.DataError as e:
    if con:
        con.rollback()
        print('There is a problem with sql:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
