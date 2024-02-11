import cx_Oracle
try:
  con = cx_Oracle.connect('scott/tiger@localhost/orcl')
  #con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
  cursor=con.cursor()
  cursor.execute('select * from student')
  rows=cursor.fetchall()
  for row in rows:
    print('Student Number:',row[0])
    print('Student Name:',row[1])
    #print('Student Fee:',row[2])
    print()


except cx_Oracle.DatabaseError as e:
  if con:
    con.rollback()
    print('There is a problem:',e)
finally:
  if cursor:
    cursor.close()
  if con:
    con.close()
    