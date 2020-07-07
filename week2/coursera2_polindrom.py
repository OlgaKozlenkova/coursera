k = int(input())
q = 0
i = 1
while i <= k:
    num1 = i
    num2 = 0
    while num1 > 0:
        balance = num1 % 10
        num1 = num1 // 10
        num2 = num2 * 10
        num2 += balance
        if num2 == i:
            q += 1
    i += 1
print(q)
