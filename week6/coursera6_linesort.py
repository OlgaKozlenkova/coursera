def CountSort(a):
    new_sorted_list = [0] * 101
    for now in a:
        new_sorted_list[now] += 1
    for elem in range(len(new_sorted_list)):
        for i in range(new_sorted_list[elem]):
            print(elem, end=" ")


my_list = list(map(int, input().split()))
CountSort(my_list)
