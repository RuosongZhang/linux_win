import json, socket

s = socket.socket()
s.connect(('172.28.1.112', 9527))

data = {'type':'object_sort'}

send_data = json.dumps(data)

s.sendall(send_data + '\n')
while True:
    data['content'] = raw_input('Input: \n>>> ')
    send_data = json.dumps(data)
    s.sendall(send_data + '\n')
