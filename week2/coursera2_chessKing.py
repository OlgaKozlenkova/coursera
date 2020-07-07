x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
differenceX12 = abs(x1 - x2)
differenceY12 = abs(y1 - y2)
if differenceX12 <= 1 and differenceY12 <= 1:
    print("YES")
else:
    print("NO")
