import math

a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
square = math.sqrt(p * (p - a) * (p - b) * (p - c))
if square % 
print(square)
