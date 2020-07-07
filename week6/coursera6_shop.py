size_foot = int(input())
shoe_size = list(map(int, input().split()))
shoe_size.sort()
pairs = 0
k = 0
for i in range(len(shoe_size)):
    if shoe_size[i] < size_foot:
        continue
    elif shoe_size[i] == k:
        continue
    elif shoe_size[i] == size_foot:
        pairs += 1
        k = shoe_size[i]
    elif shoe_size[i] - k >= 3:
        pairs += 1
        k = shoe_size[i]
print(pairs)

# n = int(input())
# a = list(map(int, input().split()))
# new = 0  # s4et4ik par
# s = 0
# a.sort()  # sortiruem spisok
# for i in range(len(a)):
#    if a[i] < n:  # esli tekushee 4islo iz spiska menshe n CONTINUE
#        continue
#    elif a[i] == s:
#        continue
#    elif a[i] == n:
#        new += 1
#        s = a[i]
#    elif a[i] - s >= 3:
#        new += 1
#        s = a[i]
# print(new)
