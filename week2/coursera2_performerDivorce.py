initial_num = int(input())
total_num = int(input())
while initial_num != total_num:
    if initial_num // 2 >= total_num and initial_num % 2 == 0:
        initial_num //= 2
        print(":2")
    else:
        initial_num -= 1
        print("-1")
