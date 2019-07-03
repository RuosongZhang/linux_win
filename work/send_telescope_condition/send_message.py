#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import datetime
import time
from corp_wechat_message import Wechat
from obervation_condition import *
def send_message_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
        #req = request.Request("https://hooks.slack.com/services/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",
        #req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

wx = Wechat()

message = obervartion_condition()
message_b = []
a = message.keys()
for i in a:
    message_b.append('%s=%s' % (i,message[i]))

x = ' , '.join(message_b)

send_message_to_slack(x)
wx.send_data(x)

print('sent successd')

