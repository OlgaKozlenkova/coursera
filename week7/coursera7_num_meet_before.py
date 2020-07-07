new_list = list(map(int, input().split()))
new_set = set()
for elem in new_list:
    if elem in new_set:
        print("YES")
    else:
        print("NO")
        new_set.add(elem)
