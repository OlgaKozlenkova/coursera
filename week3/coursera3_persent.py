p, x, y = int(input()), int(input()), int(input())
price = x * 100 + y
wholePrice = int(price * (100 + p) / 100)
print(wholePrice // 100, wholePrice % 100)
