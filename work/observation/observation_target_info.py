#!/use/bin/python
# -*- coding: utf-8 -*-


import psycopg2

#from pg_admin_bj import pg_admin

#conn = pg_admin().pg_conn()

conn = psycopg2.connect(database="gwacyw",user="yunwei",password="gwac1234",host="10.0.10.236",port="5432")
print('\n')
print("Opened database successfully!")

print('\n')

cur = conn.cursor()

cur.execute("SELECT observer,obj_name, objra, objdec, objepoch, imgtype, filter,\
 expdur, frmcnt, priority FROM object_list_all,object_list_current WHERE object_list_all.\
 obj_id=object_list_current.obj_id ORDER BY objra;")

rows = cur.fetchall()
'''print( 'observer, obj_ra, obj_dec, obj_epoch, filter, expdur, frmcnt, priority')'''
for row in rows:
    print ('observer=', row[0],)
    print ('obj_name=', row[1],)
    print ('objra=', row[2],)
    print ('objdec=', row[3])
    print ('objepoch=', row[4],)
    print ('imgtype=', row[5],)
    print ('filter=', row[6],)
    print ('expdur=', row[7],)
    print ('frmcnt=', row[8],)
    print ('priority=', row[9])
    print ('\n')
#    print (row)
