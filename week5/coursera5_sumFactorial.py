n = int(input())
sum_factorial = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_factorial += factorial
print(sum_factorial)
