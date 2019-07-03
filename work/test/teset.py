import time
import datetime
text = open('/mnt/c/linux_win/work/data/shift_GWAC_weekly_2019_may.txt')
line = text.readline()
b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
c = (datetime.datetime.now() + datetime.timedelta(days= +7)).strftime("%Y-%m-%d")
print(b)
print(c)
while line:
    #print(line)
    if b in line.split()[1]:
        print(line)
    if c in line.split()[1]:
        print(line)
    line = text.readline()
text.close()
print('ojbk')