import datetime

while True:
    while True:
        time_now = (datetime.datetime.now() + datetime.timedelta(hours= -10)).strftime("%H:%M:%S")
        if time_now >= '11:37:50'and time_now <= '11:37:51':
            print('xxx')
        break