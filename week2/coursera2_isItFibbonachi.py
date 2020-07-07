new_numb = int(input())
fib1 = 1
fib2 = 1
ind = 2
found = False
while True:
    if fib1 > new_numb:
        break
    else:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        ind += 1
        if fib2 == new_numb:
            print(ind)
            found = True
if not found:
    print(-1)
