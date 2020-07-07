def lagrange(n):
    for i in range(4):
        s = int(n ** 0.5)
        n = n - s ** 2
        if s != 0:
            print(s)


n = int(input())
lagrange(n)
