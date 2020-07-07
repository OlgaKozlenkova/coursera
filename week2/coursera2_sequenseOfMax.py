num = -1
count = 1
prev_num = -1
new_count = -1
while num != 0:
    num = int(input())
    if num == prev_num:
        count += 1
    else:
        prev_num = num
        if count > new_count:
            new_count = count
        count = 1
if count >= new_count:
    print(count)
else:
    print(new_count)
