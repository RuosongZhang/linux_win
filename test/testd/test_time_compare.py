import time

print(time.time())
a = '2019-05-28 14:36:56'
b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(b)

print(a > b)