n = int(input())
all_num = set(range(1, n + 1))
while True:
    question = input()
    if question == "HELP":
        break
    question = {int(x) for x in question.split()}
    answer = input()
    if answer == "YES":
        all_num &= question
    else:
        all_num -= question
print(*sorted(all_num))
