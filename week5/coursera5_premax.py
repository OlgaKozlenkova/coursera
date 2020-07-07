new_list = list(map(int, input().split()))
len_new_list = len(new_list)
for i in range(1, len_new_list):
    if new_list[i] > new_list[i - 1]:
        print(new_list[i], end=" ")
