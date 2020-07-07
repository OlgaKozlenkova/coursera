import math

a, b, c = float(input()), float(input()), float(input())
diskriminant = b ** 2 - 4 * a * c

if diskriminant > 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif diskriminant == 0:
    x_one = -b / (2 * a)
    print(x_one)
