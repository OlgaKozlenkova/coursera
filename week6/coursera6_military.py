# town_numb = int(input())
# towns = list(map(int, input().split()))
# bomb_numb = int(input())
# bombs = list(map(int, input().split()))
# for i in range(len(bombs)):
#    bombs[i] = [i + 1, bombs[i]]
#
#
# def func_sort(x):
#    return x[1]
#
#
# bombs.sort(key=func_sort)
# # bombs.sort(key=lambda x: x[1])
#
#
# def find_value(x):
#    if x < bombs[0][1]:
#        return bombs[0][0]
#    if x > bombs[-1][1]:
#        return bombs[-1][0]
#    l = 0
#    r = len(bombs) - 1
#    # bombs[l][1] < x
#    while r - l > 1:
#        bomb_numb = (r + l) >> 1
#        if bombs[bomb_numb][1] < x:
#            l = bomb_numb
#        else:
#            r = bomb_numb
#    if x - bombs[l][1] < bombs[r][1] - x:
#        return bombs[l][0]
#    else:
#        return bombs[r][0]
#
#
# print(*[find_value(v) for v in towns])


num_city = int(input())
dist_city = list(map(int, input().split()))
num_bombs = int(input())
dist_bomb = list(map(int, input().split()))
cities = []
bombs = []
for i in range(num_city):
    data_city = [i + 1, dist_city[i], 0]
    cities.append(data_city)
cities.sort()
for j in range(num_bombs):
    data_bomb = [j + 1, dist_bomb[j]]
    bombs.append(data_bomb)
bombs.sort()

start = 0  # Переменная для начала вложенного цикла
for i in range(num_city):
    idx = 0  # Точка нахождения нужного бомбоубежища
    minimum = 10e10  # Чтобы минимум был точно больше любого найденного
    for j in range(start, num_bombs):
        dist = abs(cities[1][i] - bombs[1][j])
        if dist < minimum:  # Либо обновляем минимум и номер бомбоубежища
            idx = j
            minimum = dist
            cities[2][i] = bombs[1][j]
        else:  # Либо заканчиваем цикл
            break
    start = idx

cities(key=lambda idx: idx[0])

print(*[i[2] for i in cities])


# n = int(input())
# np = list(map(int, input().split()))
# Здесь создали 3-е поле для номера бомбоубежища
# for i in range(n):
#   np[i] = [np[i], i + 1, 0]
# np.sort()
#
# m = int(input())
# bu = list(map(int, input().split()))
# for i in range(m):
#   bu[i] = [bu[i], i + 1]
# bu.sort()#
# Переменная для начала вложенного цикла
# start = 0
# for i in range(n):
# Точка нахождения нужного бомбоубежища
#     idx = 0
# Чтобы минимум был точно больше любого найденного
#     minimum = 10e10
#     for j in range(start, m):
#         tmp = abs(np[i][0] - bu[j][0])
# Либо обновляем минимум и номер бомбоубежища
#       if tmp < minimum:
#           idx = j
#           minimum = tmp
#           np[i][2] = bu[j][1]
# Либо заканчиваем цикл
#       else:
#           break
# Переопределяем начало вложенного цикла
#   start = idx#
# np.sort(key=lambda idx: idx[1])
# Получаем упорядоченный согласно порядка ввода список населённых пунктов и
# назначенных им бомбоубежищ. В качестве отладки такое:
# print(*[i[2] for i in np])
