a, b, c = int(input()), int(input()), int(input())
if a != 0 and b != 0 and c != 0:
    if a // b == 1 and a // c == 1 and b // c == 1:
        print("3")
    elif b // c == 1 or a // c == 1 or a // b == 1:
        print("2")
    else:
        print("0")
else:
    if a == 0 and c == 0 and b == 0:
        print("3")
    elif b == 0 and a == 0 or c == 0:
        print("2")
    elif a == 0 and c == 0 or b == 0:
        print("2")
    else:
        print("0")
