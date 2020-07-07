first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
union_list = []
i = 0
j = 0
while (i < len(first_list)) and (j < len(second_list)):
    if first_list[i] > second_list[j]:
        j += 1
    elif first_list[i] < second_list[j]:
        i += 1
    else:
        union_list.append(first_list[i])
        i += 1
        j += 1
print(*union_list)
