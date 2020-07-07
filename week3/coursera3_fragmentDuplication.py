string = input()
first_entry = string.find("h")
last_entry = string.rfind("h")
nex_first = first_entry + 1
first_part_of_string = string[:last_entry]
middle_part_of_string = string[nex_first:last_entry]
last_part_of_string = string[last_entry:]
print(first_part_of_string, middle_part_of_string, last_part_of_string, sep="")
