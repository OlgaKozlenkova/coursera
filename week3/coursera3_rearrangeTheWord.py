string = input()
split = string.find(" ")
first_word = string[:split]
next_word = split + 1
second_word = string[next_word:]
print(second_word, first_word)
