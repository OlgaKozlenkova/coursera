new_list = list(map(int, input().split()))
len_new_list = len(new_list)
q = 0
for i in range(len_new_list):
    if new_list[i] > 0:
        q += 1
print(q)
