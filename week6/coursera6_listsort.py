list_of_names = open("input.txt", "r", encoding="utf8")
list_of_names_output = open("output.txt", "w", encoding="utf8")
new_list = []
for line in list_of_names:
    one_line = line.strip().split()
    del one_line[2]
    new_list.append(one_line)
new_list.sort(key=lambda x: x[0])
for i in new_list:
    # print(*i)
    print(*i, file=list_of_names_output)
list_of_names.close()
list_of_names_output.close()


# lines = list_of_names.readlines()
# lines.sort(key=lambda x: x[0])
# for line in lines:
#    one_line = line.strip("\n").split()
#    del one_line[2]
#    print(*one_line, file=list_of_names_output)
# list_of_names.close()
# list_of_names_output.close()
