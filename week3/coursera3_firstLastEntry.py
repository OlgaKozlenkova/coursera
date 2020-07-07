string = input()
first_entry = string.find("f")
last_entry = string.rfind("f")
if first_entry == -1:
    print()
elif first_entry == last_entry:
    print(first_entry)
else:
    print(first_entry, last_entry)
