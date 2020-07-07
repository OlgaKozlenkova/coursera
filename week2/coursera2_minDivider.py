n = int(input())
i = 2
while n >= i:
    if n % i == 0:
        print(i)
        break
    else:
        i = i + 1
        if n % i == 0:
            print(i)
            break
