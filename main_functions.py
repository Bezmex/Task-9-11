#Функции обработки данных
import math
from array import array

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


def sum_or_dif_of_array(array1, array2):
    print("Выберите находить сумму или разность массивов:\n"
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


# Вычисление расстояния между двумя точками
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#Сверяем расстояние с данным числом
def find_points_bigger_distance(array1, array2, number_for_compare):
    # Инициализация массива для хранения результатов
    points_array = []

    for point1, point2 in zip(array1, array2):
        if distance(point1, point2) > number_for_compare:
            points_array.append((point1, point2))

    return points_array

if __name__ == "__main__":
    array1 = [(1, 2), (3, 4)]
    array2 = [(7, 8), (5, 6)]

    result = find_points_bigger_distance(array1, array2, 1)
    print(f"Пары точек: {result}")