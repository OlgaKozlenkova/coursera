new_list = list(map(int, input().split()))
q = 1
for i in range(0, len(new_list) - 1):
    if new_list[i] != new_list[i + 1]:
        q += 1
print(q)
