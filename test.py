import cx_Oracle
try:
  con = cx_Oracle.connect('scott/tiger@localhost/orcl')
  #con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
  cursor=con.cursor()
  increment=int(input('Enter Fee Increment value by:'))
  Fee_Range=int(input('Fee Range:'))
  query=f'update student set Sfee=Sfee+{increment} where Sfee<{Fee_Range}'
  cursor.execute(query)
  con.commit()
  
except cx_Oracle.DataError as e:
  if con:
    con.rollback()
    print('There is a problem with sql:',e)
finally:
  if cursor:
    cursor.close()
  if con:
    con.close()
