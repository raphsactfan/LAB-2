# Напишите программу, демонстрирующую работу try\except\finally

def divide(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        print("Ошибка при делении на ноль")
        return None
    finally:
        print("Функция выполнена")
    return answer

while True:
    print("\nДЕЛЕНИЕ ЧИСЕЛ (введите 0 для выхода)\n")
    delimoe = int(input("Введите делимое: "))
    if delimoe == 0:
        print("Выход из программы")
        break
    delitel = int(input("Введите делитель: "))
    chastnoe = divide(delimoe, delitel)

    if chastnoe is not None:
        print("Частное - ", chastnoe)
