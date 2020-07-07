def combination(n, k):
    if k == 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


n = int(input())
k = int(input())
print(combination(n, k))
