a = int(input())
b = int(input())
c = int(input())
if (a < b + c) and (b < a + c) and (c < a + b):
    if max(a, b, c) == a:
        cosA = (c ** 2 + b ** 2 - a ** 2) / 2 * b * c
        if cosA > 0:
            print("acute")
        elif cosA < 0:
            print("obtuse")
        elif cosA == 0:
            print("rectangular")
        else:
            print("impossible")
    elif max(a, b, c) == b:
        cosA = (c ** 2 + a ** 2 - b ** 2) / 2 * a * c
        if cosA > 0:
            print("acute")
        elif cosA < 0:
            print("obtuse")
        elif cosA == 0:
            print("rectangular")
        else:
            print("impossible")
    elif max(a, b, c) == c:
        cosA = (a ** 2 + b ** 2 - c ** 2) / 2 * a * b
        if cosA > 0:
            print("acute")
        elif cosA < 0:
            print("obtuse")
        elif cosA == 0:
            print("rectangular")
        else:
            print("impossible")
else:
    print("impossible")
