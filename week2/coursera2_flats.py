firstFlat = int(input())
lastFlat = int(input())
numberOfFlats = lastFlat - firstFlat + 1
if lastFlat % numberOfFlats == 0:
    print("YES")
else:
    print("NO")
