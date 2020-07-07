new_list = list(map(int, input().split()))
for i in range(0, len(new_list) - 1, 2):
    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
print(*new_list)
