new_text = open("input.txt", "r", encoding="utf8")
word_dict = dict()
for line in new_text:
    for word in line.strip().split():
        word_dict[word] = word_dict.get(word, -1) + 1
        print(word_dict[word], end=" ")
