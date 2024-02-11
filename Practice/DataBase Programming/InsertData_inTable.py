import cx_Oracle
try:
  #con = cx_Oracle.connect('scott/tiger@localhost/orcl')
  con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
  cursor=con.cursor()
  sql="Insert into student values(:Sno,:Sname,:Sfee)"
  records=[(101,'Paul',10000),
           (202,'John',20000)]
  cursor.executemany(sql,records)
  con.commit()
  print('Records Inserted succesfully')

except cx_Oracle.DataError as e:
  if con:
    con.rollback()
    print('There is a problem with sql:',e)
finally:
  if cursor:
    cursor.close()
  if con:
    con.close()
