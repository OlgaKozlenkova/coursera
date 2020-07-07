def phib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


n = int(input())
print(phib(n))
