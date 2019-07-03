#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import time
from corp_wechat_message import Wechat

def send_message_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        #()req = request.Request("https://hooks.slack.com/services/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",
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

wx = Wechat()

a = open('/mnt/c/linux_win/work/test/data/shift_GWAC_2019_may.txt')
line = a.readline()
b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(b)
while line:
#    print(line)
    if b in line.split()[1]:
        print('ojbk')
#        print(line)
        send_message_to_slack(line)
        wx.send_data(line)
    line = a.readline()
a.close()
print('sent successd')