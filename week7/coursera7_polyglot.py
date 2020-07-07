# union = set()
# all = set()
# for i in range(int(input())):
#    m = int(input())
#    a = {input() for j in range(m)}
#    all.update(a)
#    if i == 1:
#        union.update(a)
#    else:
#        union &= a
# print(len(union))
# print("\n".join(sorted(union)))
# print(len(all))
# print("\n".join(sorted(all)))


num_schoolkid = int(input())
languages = []
common_lang = set()
for i in range(num_schoolkid):
    num_lang = int(input())
    for j in range(num_lang):
        lang_type = input()
        languages.append(lang_type)
for lang in languages:
    if languages.count(lang) == num_schoolkid:
        common_lang.add(lang)
print(len(common_lang))
print(*common_lang, sep="\n")
print(len(set(languages)))
print(*set(languages), sep="\n")
