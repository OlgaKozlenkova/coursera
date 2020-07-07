first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
print(len(set(first_list) & set(second_list)))
