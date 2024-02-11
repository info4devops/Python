# Delete student data whose fee is less than/greterthan the specified fee

import cx_Oracle

try:
    #con = cx_Oracle.connect('scott/tiger@localhost/orcl')
    con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
    cursor = con.cursor()
    cutoff_fee = int(input('Enter Cut off Fee::'))
    query = f'Delete from student where Sfee <{cutoff_fee}'
    cursor.execute(query)
    con.commit()

except cx_Oracle.DataError as e:
    if con:
        con.rollback()
        print('There is a problem with sql:', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
