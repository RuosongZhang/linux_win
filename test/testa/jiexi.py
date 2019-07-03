import time

a = []
for i in range(1,11):
    a.append(i)

print(a)

b = [i for i in range(1,11)]

print(b)


c = []
t0 = time.clock()
for i in range(1,200000):
    c.append(i)
print(time.clock() - t0, "seconds process time")

t0 = time.clock()
d = [i for i in range(200000)]

print(time.clock() - t0, "seconds process time")

e = [j**2 for j in range(1,10)]
print(e)

f = [j+1 for j in range(1,10)]
print(f)

k = [n for n in range(1,10) if n % 2 ==0]
print(k)

h = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(h)

j = {i:i+1 for i in range(4)}
print(j)

g = {i:j for i,j in zip(range(1,6),'abcde')}
print(g)
m = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(m)
