def the_same_sing(new_list):
    length = len(new_list)
    for i in range(1, length):
        # fmt: off
        if new_list[i] < 0 and \
           new_list[i - 1] < 0 or \
           new_list[i] > 0 and \
           new_list[i - 1] > 0:
            return print(new_list[i - 1], new_list[i])
    return print()


new_list = list(map(int, input().split()))
the_same_sing(new_list)
