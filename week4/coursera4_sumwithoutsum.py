def sum(a, b):
    if b > 0:
        return sum(a + 1, b - 1)
    else:
        return a


a, b = int(input()), int(input())
print(sum(a, b))
