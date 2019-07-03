# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random
#bot = Bot()
bot = Bot(console_qr=2,cache_path="botoo.pkl")

#my_friend = bot.friends().search('承云')
#my_friend.send('hello')

myself = bot.self

bot.file_helper.send('hello')
