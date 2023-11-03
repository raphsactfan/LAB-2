# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения ax^2+bx+c=0 и возвращает его корни в порядке возрастания.
# 2  -3  1
# 1 -2 -3

from math import sqrt

def solve(a, b, c):
    D = b*b - 4*a*c
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    if x1 == x2:
        print("Корень: ", x1)
    else:
        roots = [x1, x2]
        roots.sort()
        print("Корни:", ', '.join(map(str, roots)))

while True:
    try:
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))
        c = int(input("Введите значение c: "))
        print(f"\nУравнение {a}x^2 + {b}x + {c} = 0\n")
        try:
            solve(a, b, c)
        except ValueError:
            print("Выражение не определено на множестве действительных чисел\n")
    except ValueError:
        print("Ошибка: Введите целые числа для a, b и c.")
