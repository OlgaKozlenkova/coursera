n = int(input())
fib1 = 1
fib2 = 1
i = 0
while True:
    if i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    else:
        break
print(fib2)
