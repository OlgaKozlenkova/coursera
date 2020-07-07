from math import sqrt

middle_math = 0
dev = 0
x = -1
n = 0
sum_sqrt = 0
while x != 0:
    x = int(input())
    sum_sqrt += x ** 2
    n += 1
    dev = sum_sqrt / n
    middle_math += (x - dev) ** 2
print(sqrt(middle_math / n))
