a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - c * b
if delta != 0:
    delta_x = d * e - b * f
    delta_y = a * f - c * e
    x = delta_x / delta
    y = delta_y / delta
print(x, y)
