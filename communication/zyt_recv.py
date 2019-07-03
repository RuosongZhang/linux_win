# -*- coding:utf-8 -*-
import json, socket, time

s = socket.socket()
s.connect(('172.28.1.112', 9527))

send_data = json.dumps({'type':'object_sort'})

s.sendall(send_data + '\n')
while True:
    recv = s.recv(5120)
    try:
        recv = json.loads(recv)
        print(time.ctime())
        print('content: ', recv['content'])
        print('')
    except:
        print(recv)
