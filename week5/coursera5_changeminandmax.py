new_list = list(map(int, input().split()))
min_ind = 0
max_ind = 0
for i in range(len(new_list)):
    if new_list[i] > new_list[max_ind]:
        max_ind = i
    if new_list[i] < new_list[min_ind]:
        min_ind = i
new_list[min_ind], new_list[max_ind] = new_list[max_ind], new_list[min_ind]
print(" ".join(str(i) for i in new_list))
