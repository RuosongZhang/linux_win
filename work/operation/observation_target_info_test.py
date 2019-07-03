#!/use/bin/python
# -*- coding: utf-8 -*-


import psycopg2
from urllib import request, parse
    
import json

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

def send_message_to_slack(*text):
    

    post = {"text": "{0}".format(*text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))





for rowe in rows:
    send_message_to_slack ('observer=', rowe[0],)
    send_message_to_slack ('obj_name=', rowe[1],)
    send_message_to_slack ('objra=', rowe[2],)
    send_message_to_slack ('objdec=', rowe[3])
    send_message_to_slack ('objepoch=', rowe[4],)
    send_message_to_slack ('imgtype=', rowe[5],)
    send_message_to_slack ('filter=', rowe[6],)
    send_message_to_slack ('expdur=', rowe[7],)
    send_message_to_slack ('frmcnt=', rowe[8],)
    send_message_to_slack ('priority=', rowe[9])
    send_message_to_slack ('\n')