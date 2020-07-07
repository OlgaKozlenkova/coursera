import math


def trianglePerimetr(x1, y1, x2, y2, x3, y3):
    segmentLenth_a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    segmentLenth_b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    segmentLenth_c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    perimetr = segmentLenth_a + segmentLenth_b + segmentLenth_c
    return perimetr


x1, y1, x2, y2, x3, y3 = (
    float(input()),
    float(input()),
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)

print("{0:.6f}".format(trianglePerimetr(x1, y1, x2, y2, x3, y3)))
