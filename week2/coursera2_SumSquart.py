n = int(input())
sum = 0
i = 1
while True:
    if i <= n:
        k = i ** 2
        sum += k
        i = i + 1
    else:
        print(sum)
        break
