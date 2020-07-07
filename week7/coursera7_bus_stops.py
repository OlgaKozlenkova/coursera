stops = list(map(int, input().split()))
bus1 = set()
bus2 = set()
if stops[0] < stops[1]:
    for i in range(stops[0], stops[1] + 1, 1):
        bus1.add(i)
else:
    for i in range(stops[1], stops[0] + 1, 1):
        bus1.add(i)
if stops[2] < stops[3]:
    for j in range(stops[2], stops[3] + 1, 1):
        bus2.add(j)
else:
    for j in range(stops[3], stops[2] + 1, 1):
        bus2.add(j)
print(len(bus1 & bus2))
