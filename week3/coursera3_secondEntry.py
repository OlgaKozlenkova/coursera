string = input()
first_entry = string.find("f")
second_entry = string.find("f", first_entry + 1)
if first_entry == -1:
    print("-2")
elif first_entry == second_entry:
    print("-1")
else:
    print(second_entry)
