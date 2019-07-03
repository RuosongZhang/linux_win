#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import time
import datetime
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

text = open('/mnt/c/linux_win/work/data/shift_GWAC_weekly_2019_may.txt')
line = text.readline()
b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
c = (datetime.datetime.now() + datetime.timedelta(days= +7)).strftime("%Y-%m-%d")
print(b)
print(c)
while line:
    #print(line)
    if b in line.split()[1]:
        send_message_to_slack(line)
        wx.send_data(line)
        #print(line)
    if c in line.split()[1]:
        send_message_to_slack(line)
        wx.send_data(line)
        #print(line)
    line = text.readline()
text.close()
print('send successd')