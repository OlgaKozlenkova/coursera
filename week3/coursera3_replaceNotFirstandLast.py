string = input()
first_entry = string.find("h")
last_entry = string.rfind("h")
first = first_entry + 1
string_slice = string[first:last_entry]
change_h = string_slice.replace("h", "H")
print(string[:first], change_h, string[last_entry:], sep="")
