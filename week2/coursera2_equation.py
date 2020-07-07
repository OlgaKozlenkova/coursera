a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print("INF")
elif a == 0 or b * c == d * a or -b % a != 0:
    print("NO")
elif b * c != d * a and -b % a == 0:
    print(int(-b // a))
