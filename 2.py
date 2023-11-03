# Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся множество, то найти произведение всех его чисел.
# Если список, то удалить все нулевые элементы, найти произведение между первым и вторым положительными элементами.
# Число – определить количество разрядоВ.
# Строка – найти количество чисел в строке.
# Сделать проверку со всеми этими случаями.

def func(x):

    if type(x) is set:
        proizvedenie = 1
        for i in x:
            if i.isdigit():
                proizvedenie = proizvedenie * float(i)
        print("\nПроизведение всех чисел множества =", proizvedenie)

    elif type(x) is list:
        x = [i for i in x if i != '0']
        print("Список без нулей:", x)
        poz_1 = None
        poz_2 = None
        for i in x:
            try:
                num = int(i)
                if num > 0:
                    if poz_1 is None:
                        poz_1 = num
                    elif poz_2 is None:
                        poz_2 = num
                    else:
                        break
            except ValueError:
                pass
        if poz_1 is None:
            print("В списке нет положительных чисел")
        elif poz_2 is None:
            print("В списке только одно положительное число")
        else:
            summa = poz_1 + poz_2
            print("Сумма первого и второго положительного числа равна", summa)

    elif type(x) is int:
        raz = 0
        while x > 0:
            x = x // 10
            raz += 1
        print("Количество разрядов числа =", raz)

    elif type(x) is str:
        kolvo = 0
        number = ''      #строка с текущим числом
        for i in x:
            if i.isdigit():
                number += i
            elif number:
                kolvo += 1
                number = ''
        if number:
            kolvo += 1
        print("количество чисел - ", kolvo)

while True:
    print('''\nЧто передать в функцию?
1 - множество
2 - список
3 - число
4 - строку
5 - выйти из программы''')
    choice = input()

    if choice == '1':
        input_set = input("Введите множество: ")
        a = set(input_set.split())
        print("\nМножество:", a)
        func(a)

    elif choice == '2':
        input_list = input("Введите список: ")
        b = list(input_list.split())
        print("\nИсходный список:", b)
        func(b)

    elif choice == '3':
        try:
            c = int(input("Введите число: "))
            print("\nЧисло:", c)
            func(c)
        except:
            print("Ошибка, введите число")

    elif choice == '4':
        d = input("Введите строку: ")
        print("\nСтрока: ", d)
        func(d)

    elif choice == '5':
        print("Выход из программы")
        break

    else: print("\nОшибка ввода")




