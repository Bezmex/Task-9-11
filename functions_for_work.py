#Функции ввода

import random
def is_int(choice):
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

#Ввод массива
def input_array():
    input_str = input("Введите числа через пробел для массива: ")
    number_array = [int(number) for number in input_str.split()]
    return number_array


#Задание массива чисел рандомно
def random_array(length):
    number_array = [random.randint(1, 100) for _ in range(length)]
    return number_array

#Задаем большое число и преобразуем его в массив
def input_large_number_for_arr():
    number_str = input("Введите большое число: ")
    number_array = [int(number) for number in number_str]
    return number_array

#Рандомно генерируем массив из длины числа
def generate_random_number_for_arr(length):
    number_array = [random.randint(0, 9) for _ in range(length)]
    return number_array



