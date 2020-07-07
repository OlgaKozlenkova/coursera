n = int(input())
k = 1
if n != 1:
    while True:
        if 2 ** k >= n:
            print(k)
            break
        else:
            k = k + 1
else:
    print(0)
