string = input()
new_string = string[1:-1]
if len(string) > 1:
    print(string[0], new_string.replace("", "*"), string[-1], sep="")
else:
    print(string[0])
