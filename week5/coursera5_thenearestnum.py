length = int(input())
original = list(map(int, input().split()))
original = original[:length]

target = int(input())
found = original[0]

for i in original[1:]:
    if abs(i - target) < abs(target - found):
        found = i

print(found)
# n = int(input())
# new_list = list(map(int, input().split()))
# k = int(input())
# for i in range(len(new_list)):
#    if abs(new_list[i] - k) == 0:
#        a = new_list[i]
#        break
#    elif abs(new_list[i] - k) == 1:
#        a = new_list[i]
#        break
#    elif 1 < abs(new_list[i] - k) < 5:
#        a = new_list[i]
#        break
#    elif abs(new_list[i] - k) >= 5:
#        a = max(new_list)
# print(a)

#
# N = int(input())
# myList = list(map(int, input().split()))
# x = int(input())
# newList = []
# if myList.count(x) > 0:
#    print(x)
# else:
#    for i in range(N):
#        newList.append(abs(myList[i] - x))
#        ind = newList.index(min(newList))
# print(myList[ind])
#

# length = int(input())
# original = list(map(int, input().split()))
# original = original[:length]
#
# target = int(input())
# found = original[0]
#
# for i in original[1:]:
#    if i > target - 1 or i < target + 1:
#        found = i
#
#    if found == target:
#        break
#
# print(found)
