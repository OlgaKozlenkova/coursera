candidats_list = open("input.txt", "r", encoding="utf8")
candidats_list_out = open("output.txt", "w", encoding="utf8")
lines = candidats_list.readlines()
candidats_dict = dict()
voises = 0
for line in lines:
    name, voises = line.strip(), voises
    candidats_dict[name] = candidats_dict.get(name, 0) + 1
    voises += 1
candidats = sorted(candidats_dict.items(), key=lambda x: x[1], reverse=True)
persent = candidats[0][1] / voises * 100
if persent > 50:
    print(candidats[0][0], file=candidats_list_out)
else:
    for name, voises in candidats[:2]:
        print(name, file=candidats_list_out)
