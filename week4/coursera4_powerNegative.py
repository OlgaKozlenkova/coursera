def power(a, n):
    if n == 0:
        return 1
    return a * pow(a, n - 1)


a = float(input())
n = float(input())
print(power(a, n))
