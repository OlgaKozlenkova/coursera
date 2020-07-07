def IsAscending(sequence):
    i = 1
    length = len(sequence)
    while i <= length - 1 and sequence[i] > sequence[i - 1]:
        i += 1
    if i == length:
        return True


sequence = list(map(int, input().split()))
if IsAscending(sequence):
    print("YES")
else:
    print("NO")
