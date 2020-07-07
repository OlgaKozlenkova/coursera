import math


def distance(x1, y1, xc, yc):
    delta_x = (abs(x1 - xc)) ** 2
    delta_y = (abs(y1 - yc)) ** 2
    dist = math.sqrt(delta_x + delta_y)
    return dist


def IsPointInCircle(x1, y1, xc, tc, r):
    return distance(x1, y1, xc, yc) <= r


x1 = float(input())
x2 = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if IsPointInCircle(x1, x2, xc, yc, r):
    print("YES")
else:
    print("NO")
