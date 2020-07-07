n = int(input())
new_list = list(map(int, input().split()))
new_list = new_list[:n]
new_list.sort()
print(" ".join(map(str, new_list)))
