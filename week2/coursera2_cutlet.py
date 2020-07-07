k = int(input())
m = int(input())
n = int(input())
if n <= k:
    times = 2 * m
elif n * 2 % k == 0:
    times = m * (n * 2 // k)
else:
    times = m * (1 + (n * 2 // k))
print(times)
