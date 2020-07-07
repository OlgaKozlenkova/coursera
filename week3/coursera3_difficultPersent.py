p, x, y, k = int(input()), int(input()), int(input()), int(input())
price = x * 100 + y
i = 1
while i <= k:
    whole_price = int(price + price * p / 100)
    price = whole_price
    i += 1
print(price // 100, price % 100)
