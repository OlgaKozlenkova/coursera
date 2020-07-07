old_list = list(map(int, input().split()))
length = int(len(old_list) / 2)
j = -1
for i in range(0, length):
    old_list[i], old_list[j] = old_list[j], old_list[i]
    j -= 1
print(*old_list)
