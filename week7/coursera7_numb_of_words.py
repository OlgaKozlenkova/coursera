text = open("input.txt", "r", encoding="utf8")
list_of_words = text.read().split()
print(len(set(list_of_words)))
