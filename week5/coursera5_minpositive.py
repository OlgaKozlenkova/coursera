my_list = list(map(int, input().split()))
length = len(my_list)
positive_list = [i for i in my_list if i > 0]
print(min(positive_list))
