a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
if a >= x and b >= x and c >= x:
    if a >= y and b >= y and c >= y:
        if a >= z and b >= z and c >= z:
            V1 = a * b * c
            V2 = x * y * z
            print(V1 // V2)
        else:
            print("0")
    else:
        print("0")
else:
    print("0")
