new_list = list(map(int, input().split()))
length = len(new_list)
q = 0
for i in range(1, length - 1):
    if new_list[i] > new_list[i - 1] and new_list[i] > new_list[i + 1]:
        q += 1
print(q)
