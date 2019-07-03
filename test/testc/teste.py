import math
a = 90
x = 9

while True:
    print(x)

    y = (x + a/x) / 2
    if abs(y-x) < Epsilon:
        break