new_list = list(map(int, input().split()))
new_one = new_list[-1]
new_list.insert(0, new_one)
new_list.pop(-1)
print(*new_list)
