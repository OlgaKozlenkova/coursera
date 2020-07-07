my_list = list(map(int, input().split()))
odd_list = [i for i in my_list if i % 2 != 0]
print(min(odd_list))
