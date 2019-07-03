import datetime
import time

a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(a)
time_now = time.strftime("%H:%M:%S", time.localtime(time.time()-3600))  # 刷新
b = time.strftime('%Y-%m-%d'  "%H:%M:%S",time.localtime(time.time()))
print(b)
print(time_now)
time_two =  'sdf'
print(time_two)

x = (datetime.datetime.now() + datetime.timedelta(hours= -1)).strftime("%H:%M:%S")
print(x)