from array import array
from functions_for_work import *

def input_numbers_mas_for_compare(array1, array2):
    """
    Функция для ввода двух массивов чисел, для сравнения
    :param array1: Массив 1
    :param array2: Массив 2
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

#Алгоритм поиска одинаковых чисел в массивах
def count_same_numbers(array1, array2):
    """
    Алгоритм поиска одинаковых чисел в двух массивах
    :param array1: Массив 1
    :param array2: Массив 2
    """
    result = 0
    for i in array1:
        for j in array2:
            if i == j or str(i)[::-1] == str(j):
                result += 1
    print("\nАлгоритм выполнен\n")
    return result


#-------------------------------------------------------------------------------------------------

def input_big_numbers_mas(array1, array2):
    """
    Функция для ввода двух массивов, представляющих большие числа
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы \n")
    option = input()
    if is_int(option):
        option = int(option)

    if option == 1:
        # Ввод двух больших чисел вручную
        array1 = input_large_number_for_arr()
        array2 = input_large_number_for_arr()
    elif option == 2:
        # Генерация двух больших чисел случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_number_for_arr(length1)
        length2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_number_for_arr(length2)

    else:
        print('error')
    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2


def sum_or_dif_of_array(array1, array2):
    """
    Алгоритм сложения/вычитания двух массивов, который возвращяет полученное значение
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите находить сумму или разность массивов:\n"
          "1. Сумму\n"
          "2. Разность")
    operation_choice = input()
    if is_int(operation_choice):
        operation_choice = int(operation_choice)

    if operation_choice == 1:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1+sum2

    elif operation_choice == 2:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1-sum2
    else:
        print("Ошибка выбора")
    print("\nАлгоритм выполнен\n")

#-------------------------------------------------------------------------------------------------


def input_points_array(array1, array2):
    """
    Алгоритм задания значений массивов точек
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы \n")
    option = input()
    if is_int(option):
        option = int(option)

    if option == 1:
        # Ввод массивов точек вручную
        array1 = input_points()
        array2 = input_points()
    elif option == 2:
        # Генерация двух больших чисел случайным образом
        amount_of_points1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_points(amount_of_points1)
        amount_of_points2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_points(amount_of_points2)

    else:
        print('error')
    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2


#Сверяем расстояние с данным числом
def find_points_bigger_distance(array1, array2, number_for_compare):
    """
    Алгоритм сравнения расстояний между точками с заданным число
    :param array1: Массив 1
    :param array2: Массив 2
    :param number_for_compare: число для сравнения, задается пользователем
    """
    # Инициализация массива для хранения результатов
    points_array = []

    for point1, point2 in zip(array1, array2):
        if distance(point1, point2) > number_for_compare:
            points_array.append((point1, point2))
    print("\nАлгоритм выполнен\n")
    return points_array

