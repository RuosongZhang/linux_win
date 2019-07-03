import time
import os


while True:
    print('game start')
    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
        if time_now == "10:00:00": 
            os.system('python3 send_observation_weekly_duty.py')
            break


    time.sleep(604500)