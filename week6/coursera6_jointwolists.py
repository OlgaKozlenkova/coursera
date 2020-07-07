def merge(a, b):
    joined_list = [0] * (len(first_list) + len(second_list))
    i = 0
    j = 0
    k = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] <= second_list[j]:
            joined_list[k] = first_list[i]
            i += 1
            k += 1
        else:
            joined_list[k] = second_list[j]
            j += 1
            k += 1
    while i < len(first_list):
        joined_list[k] = first_list[i]
        i += 1
        k += 1
    while j < len(second_list):
        joined_list[k] = second_list[j]
        j += 1
        k += 1
    return joined_list


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))


print(*merge(first_list, second_list))
