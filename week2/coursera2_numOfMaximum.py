now = -1
i = 0
nowMax = 0
while now != 0:
    now = int(input())
    if now > nowMax:
        nowMax = now
        i = 1
    elif now == nowMax:
        i += 1
print(i)
