n = int(input())
if n % 10 == 1 and n != 11:
    print(n, "korova", sep=" ")
elif n // 10 == 1 and n % 10 >= 2 and n % 10 <= 4:
    print(n, "korov", sep=" ")
elif n % 10 >= 2 and n % 10 <= 4:
    print(n, "korovy", sep=" ")
else:
    print(n, "korov", sep=" ")
