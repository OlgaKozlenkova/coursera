def IsPointInSquare(x, y):
    left_border_x1 = -1 <= x
    right_border_x1 = x <= 1
    left_border_y1 = -0.5 <= y
    right_border_y1 = y <= 0.5
    left_border_x2 = -0.5 <= x
    right_border_x2 = x <= 0.5
    left_border_y2 = -1 <= y
    right_border_y2 = y <= 1
    return (
        # fmt: off
        left_border_x1 and \
        right_border_x1 and \
        left_border_y1 and \
        right_border_y1 or \
        left_border_x2 and \
        right_border_x2 and \
        left_border_y2 and \
        right_border_y2
    )


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
