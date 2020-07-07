from collections import Counter

new_list = open("input.txt", "r", encoding="utf8")
lines = new_list.readlines()
words = []
for line in lines:
    words.extend(line.split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print("\n".join(words))
