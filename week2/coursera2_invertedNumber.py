num1 = int(input())
num2 = 0
while num1 > 0:
    balance = num1 % 10
    num1 = num1 // 10
    num2 = num2 * 10
    num2 += balance
print(num2)
