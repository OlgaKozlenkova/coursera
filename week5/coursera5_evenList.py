new_list = list(map(int, input().split()))
len_new_list = len(new_list)
for i in range(len_new_list):
    if new_list[i] % 2 == 0:
        print(new_list[i], end=" ")
