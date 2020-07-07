new_list = list(map(int, input().split()))
lenth_new_list = len(new_list)
q = 0
for i in range(0, lenth_new_list):
    if new_list[i] >= new_list[q]:
        q = i
    elif new_list[0] == max:
        q = 0
print(new_list[q], q)
