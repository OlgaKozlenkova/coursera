new_list = list(map(int, input().split()))
length = len(new_list)
for i in range(length + 1):
    maximum = max(new_list)
    max_index = new_list.index(maximum)
print(maximum, max_index)
