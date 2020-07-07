string = input()
i = 0
new_string = ""
while i < len(string):
    # for i in range(len(string)):
    if i % 3 != 0:
        new_string = new_string + string[i]
    i += 1
print(new_string)
