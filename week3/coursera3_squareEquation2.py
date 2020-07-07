import math

a, b, c = float(input()), float(input()), float(input())
diskriminant = b ** 2 - 4 * a * c

if diskriminant > 0 and a != 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1 < x2:
        print(2, x1, x2)
    else:
        print(2, x2, x1)
elif diskriminant == 0 and a != 0:
    x_one = -b / (2 * a)
    print(1, x_one)
elif a == 0 and c == 0 or a == b == c == 0:
    print(3)
elif diskriminant < 0 or a == 0 and b == 0 and c != 0:
    print(0)
elif a == 0 and c != 0 and b != 0:
    x_line = -c / b
    print(1, x_line)
elif c == 0 and a != 0 and b != 0:
    x11 = 0
    x22 = -b / a
    if x11 < x22:
        print(2, x11, x22)
    else:
        print(2, x22, x11)
