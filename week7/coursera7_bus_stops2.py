stops = list(map(int, input().split()))
if stops[0] > stops[2]:
    if stops[2] < stops[1] < stops[3]:
        print(stops[1] - stops[2])
    elif stops[2] == stops[3]:
        print(1)
    else:
        print(0)
elif stops[0] < stops[3]:
    print(stops[3] - stops[0])
elif stops[0] == stops[3]:
    print(1)
else:
    print(0)
