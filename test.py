import cx_Oracle

#con = cx_Oracle.connect('scott/tiger@localhost/orcl')
con = cx_Oracle.connect('scott/tiger@Vamsi_A/orcl')

if con is not None:
    print('Oracle Version:', con.version)
    con.close()
else:
    print('Not Connected')
