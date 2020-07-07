new_list = list(map(int, input().split()))
index = int(input())
new_list.pop(index)
print(*new_list)
