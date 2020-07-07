n = int(input())
synonyms = dict()
for i in range(n):
    key, value = input().split()
    synonyms[key] = value
word = input()
for key in synonyms:
    if key == word:
        print(synonyms[key])
    elif synonyms[key] == word:
        print(key)
