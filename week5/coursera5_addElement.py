new_list = list(map(int, input().split()))
index_new_elem = list(map(int, input().split()))
new_list.insert(index_new_elem[0], index_new_elem[1])
print(*new_list)
