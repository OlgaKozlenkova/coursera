import math


def distance(x1, y1, x2, y2):
    delta_x = (x2 - x1) ** 2
    delta_y = (y2 - y1) ** 2
    distance = math.sqrt(delta_x + delta_y)
    return distance


x1, y1, x2, y2 = (
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)
print(distance(x1, y1, x2, y2))
