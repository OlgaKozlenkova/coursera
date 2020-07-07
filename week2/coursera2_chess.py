x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
sumCoord = x1 + y1 + x2 + y2
if y1 < y2:
    if sumCoord % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
