list_of_names = open("input.txt", "r", encoding="utf8")
new_list = []
sum1 = 0
sum2 = 0
sum3 = 0
q1 = 0
q2 = 0
q3 = 0
for line in list_of_names:
    one_line = line.strip().split()
    one_line[2] = int(one_line[2])
    one_line[3] = int(one_line[3])
    new_list.append(one_line)
for line in new_list:
    if line[2] == 9:
        sum1 += int(line[3])
        q1 += 1
    elif line[2] == 10:
        sum2 += int(line[3])
        q2 += 1
    else:
        sum3 += int(line[3])
        q3 += 1
print(sum1 / q1, sum2 / q2, sum3 / q3)


# def listAverage(list):
#    sum = 0
#    for i in list:
#        sum += i
#    return sum / len(list)
#
#
# classes = {}
# inFile = open("input.txt", "r", encoding="utf8")
# for line in inFile:
#    grade, mark = line.split()[2:]
#    if grade in classes:
#        classes[grade].append(int(mark))
#    else:
#        classes[grade] = [int(mark)]
#
# for i in range(9, 12):
#    print(listAverage(classes[str(i)]), end=" ")
