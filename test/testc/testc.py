import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2 
    result = math.sqrt(dsquared)
    return result


def area(radius):
    temp = math.pi * radius**2
    return temp


def circle_area(xc, yc, xp, yp):
    print(area(distance(xc, yc, xp, yp)))
    return

circle_area(4,5,6,7)