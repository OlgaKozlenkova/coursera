import math

n = float(input())
if n % 1 != 0 and n % 1 < 0.5:
    print(math.floor(n))
else:
    print(math.ceil(n))
