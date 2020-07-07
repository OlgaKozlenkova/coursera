for i in range(10, 101):
    dozens = i // 10
    units = i % 10
    new_numb = 2 * dozens * units
    if i == new_numb:
        print(i)
