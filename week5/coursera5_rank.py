new_list = list(map(int, input().split()))
height = int(input())
num_rank = 0
for i in range(0, len(new_list)):
    if new_list[num_rank] >= height:
        num_rank += 1
print(num_rank + 1)
