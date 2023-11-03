# Найти в матрице первую строку, все элементы которой упорядочены по возрастанию.
# Изменить упорядоченность элементов этой строки на обратную

arr = [[1, 5, 0, 4],
       [2, 4, 8, 5],
       [3, 5, 7, 9],
       [1, 2, 3, 9]]

def vozrast(l):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

print("Матрица:")
for stroka in arr:
    print(stroka)
global STR
row = None
for stroka in arr:
    if vozrast(stroka):
        row = stroka
        STR = stroka
        break
if row:
    print("\nДанная строка -", row)
    row.reverse()
    STR = row
    print("\nИсправленная матрица:")
    for stroka in arr:
        print(stroka)
else:
    print("\nТакой строки нет")
