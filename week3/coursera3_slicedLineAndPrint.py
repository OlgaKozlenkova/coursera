string = input()
first_entry = string.find("h")
last_entry = string.rfind("h")
pre_last_entry = last_entry + 1
print(string[0:first_entry] + string[pre_last_entry:])
