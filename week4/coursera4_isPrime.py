from math import sqrt


def isPrime(n):
    d = 2
    while d <= sqrt(n):
        if n % d == 0:
            return False
        elif n % d != 0:
            d += 1
        else:
            return True
    return True


n = int(input())
if isPrime(n):
    print("YES")
else:
    print("NO")
