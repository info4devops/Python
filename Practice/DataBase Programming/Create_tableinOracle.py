# To create a table in oracle

import cx_Oracle
#con = cx_Oracle.connect('scott/tiger@localhost/orcl')
con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')
crsr=con.cursor()
crsr.execute('Create table student(Sno Number,Sname varchar2(12),Sfee number(10,2))')
print('Table created succesfully')
crsr.close()
con.close()