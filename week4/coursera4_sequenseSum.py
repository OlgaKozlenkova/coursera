def summa():
    n = int(input())
    if n == 0:
        return 0
    return n + summa()


print(summa())
