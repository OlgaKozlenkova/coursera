from math import sqrt


def MinDivisor(n):
    d = 2
    while n % d != 0:
        if d <= sqrt(n):
            d += 1
        else:
            return n
    return d


n = int(input())
print(MinDivisor(n))
