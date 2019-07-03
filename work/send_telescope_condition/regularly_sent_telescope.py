import time
import datetime
import os
while True:
    while True:
        #time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
        time_now = (datetime.datetime.now() + datetime.timedelta(hours= -10)).strftime("%H:%M:%S")
        #print(time_now)
        if time_now == '12:00:00':
            print('start')
            while True:
                #print('x')
                os.system('python3.6 send_message.py')
                time_second = (datetime.datetime.now() + datetime.timedelta(hours= -10)).strftime("%H:%M:%S")
                #print(time_second)
                time.sleep(3600)
                if time_second >= '20:00:00':
                    print('inter sleep')
                    break

        
                #time_second = time.strftime("%H:%M:%S", time.localtime())
        time_third = (datetime.datetime.now() + datetime.timedelta(hours= -10)).strftime("%H:%M:%S")
        
        if time_third >= '20:00:00':
            print('sleep')
            break
    time.sleep(35400)