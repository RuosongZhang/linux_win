#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import time
import os


while True:
    print('game start')
    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
        if time_now == "16:00:00": 
            os.system('python3 send_obervation_duty.py')
            break


    time.sleep(86340)