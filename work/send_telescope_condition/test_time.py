import time
from threading import Timer
timer_interval = 10
#timer_start == 16:50:00
def objk():
    print('objk')
t = Timer(timer_interval,objk)
t.start()
while True:
    time.sleep(3)
    print('zhanturosng')