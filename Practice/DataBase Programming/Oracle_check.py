# to check Oracle Version

import cx_Oracle

#con = cx_Oracle.connect('scott/tiger@localhost/orcl') # O/p: in sqlplus
#con = cx_Oracle.connect('scott/tiger@Vamsi_A/orcl') # O/p: in sqlplus

con = cx_Oracle.connect('scott/TIGER@Vamsi_A:1522/xe')  # O/p in SQL developer

if con is not None:
    print('Oracle Version:', con.version)
    con.close()
else:
    print('Not Connected')
