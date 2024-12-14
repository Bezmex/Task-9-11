#Функции обработки данных

from functions_for_work import *

#Алгоритм поиска одинаковых чисел в массивах
def count_same_numbers(array1, array2):
    result = 0
    for i in array1:
        for j in array2:
            if i == j or str(i)[::-1] == str(j):
                result += 1

    print("\nАлгоритм выполнен\n")
    return result


def input_numbers_mas(array1, array2):
    """
    Функция для ввода двух массивов чисел.
    """

    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)

    if option == 1:
        # Самостоятельный ввод двух числовых массивов
        array1 = input_array()
        array2 = input_array()

    elif option == 2:
        # Генерация двух числовых массивов случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве 1: "))
        array1 = random_array(length1)
        length2 = int(input("Введите количество цифр в случайном массиве 2: "))
        array2 = random_array(length2)
    else:
        print('error')
    print("\nПервый массив:", array1)
    print("Второй массив:", array2)
    return array1, array2

if __name__ == "__main__":
    array1 = []
    array2 = []
    input_numbers_mas(array1, array2)
