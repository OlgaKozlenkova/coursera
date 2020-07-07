def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def ReduceFraction(n, m):
    if n % gcd(n, m) == 0 and m % gcd(n, m) == 0:
        p = n // gcd(n, m)
        q = m // gcd(n, m)
        return p, q
    elif gcd(m, n % m) == 1:
        return n, m


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
