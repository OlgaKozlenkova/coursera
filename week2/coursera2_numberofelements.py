num = int(input())
i = 0
while num != 0:
    next = int(input())
    if next != 0 and num < next:
        i += 1
    num = next
print(i)
