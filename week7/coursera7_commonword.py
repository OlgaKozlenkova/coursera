new_list = open("input.txt", "r", encoding="utf8")
lines = new_list.readlines()
common_words = dict()
maximum = 0
for line in lines:
    for word in line.split():
        common_words[word] = common_words.get(word, 0) + 1
        if common_words[word] > maximum:
            maximum = common_words[word]
for key, value in sorted(common_words.items()):
    if value == maximum:
        print(key)
        break
