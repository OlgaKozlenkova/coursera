def konkurs(k, list):
    # количество абитуриентов меньше чем свободных мест, тогда выводим 0
    if len(list) <= k:
        return 0
    # если средний бал за три экзамена у всех одинаковый и является макс
    # (сравниваем первый и последний элементы в отсортитрованном списке)
    elif list[0] == list[k]:
        return 1
    # находим проходной балл и возващаем наибольшее значение
    for i in range(k, 0, -1):
        if list[i] < list[i - 1]:
            return list[i - 1]


inFile = open("input.txt", "r", encoding="utf8")
outFile = open("output.txt", "w", encoding="utf8")
k = int(inFile.readline())
list = []
# перебираем каждую строку и вырезаем последние три элемента
for line in inFile:
    a, b, c = [int(i) for i in line.split()[-3:]]
    # проверяем на условие проходимости
    if a > 39 and b > 39 and c > 39:
        list.append(a + b + c)  # создаем список сумм баллов
inFile.close()
list.sort(reverse=True)  # сортируем от большего балла к меньшему
print(konkurs(k, list), file=outFile)  # вызываем функцию и считаем
outFile.close()
