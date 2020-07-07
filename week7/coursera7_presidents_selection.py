candidats = open("input.txt", "r", encoding="utf8")
lines = candidats.readlines()
candidats_list = dict()
for line in lines:
    name, voices = line.strip().split()
    candidats_list[name] = candidats_list.get(name, 0) + int(voices)
for name, voices in sorted(candidats_list.items()):
    print(name, voices)
