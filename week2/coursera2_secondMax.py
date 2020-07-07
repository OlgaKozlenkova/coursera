max, premax = -1, -1
while True:
    n = int(input())
    if n == 0:
        break
    elif n >= max:
        premax, max = max, n
    elif n >= premax:
        premax = n
print(premax)
