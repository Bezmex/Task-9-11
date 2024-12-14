from main_functions import *
from functions_for_work import *
from menu_interface import *

def menu():
    #Переменные для работы
    array1 = []
    array2 = []
    menu_choice = ''
    task_choice = ''

    #Флаги для проверки выполнения пунктов меню
    is_task_selected = False
    is_info_input = False
    is_algoritm_done = False

    while 1:
        show_menu()
        menu_choice = input("\nВыберите пункт для дальнейшей работы: ")
        if is_int(menu_choice):
            menu_choice = int(menu_choice)

        if menu_choice == 1:
            show_tasks()
            task_choice = input("\nВведите номер выбранной задачи: ")
            if is_int(task_choice):
                task_choice = int(task_choice)
                is_task_selected = True
                print("\nЗадача выбрана, переходите к заполнению исходных данных\n")
            else:
                print("\nОшибка выбора\n")

        elif menu_choice == 2:
            if is_task_selected:
                if task_choice == 1:
                    array1, array2 = input_big_numbers_mas(array1, array2)
                    is_info_input = True
                if task_choice == 2:
                    array1, array2 = input_numbers_mas_for_compare(array1, array2)
                    is_info_input = True
                if task_choice == 3:
                    array1, array2 = input_points_array(array1, array2)
                    is_info_input = True
            else:
                print("\nСначала выберите задание\n")

        elif menu_choice == 3:
            if is_task_selected and is_info_input:
                if task_choice == 1:
                    result = sum_or_dif_of_array(array1, array2)
                    is_algoritm_done = True
                if task_choice == 2:
                    result = count_same_numbers(array1, array2)
                    is_algoritm_done = True
                if task_choice == 3:
                    result = find_points_bigger_distance(array1, array2)
                    is_algoritm_done = True
            else:
                print("\nСначала введите данные для выполнения алгоритма\n")

        elif menu_choice == 4:
            if is_algoritm_done:
                if task_choice == 1:
                    print(f"\nРезультат работы алгоритма по сложению/вычитанию массивов: {result}")
                if task_choice == 2:
                    print(f"\nКоличество общих чисел у двух массивов: {result}")
                if task_choice == 3:
                    print(f"\nСписок точек, удовлетворяющих условию: {result}")
            else:
                print("\nСначала выполните алгоритм\n")

        elif menu_choice == 5:
            break
        else:
            print("\nОшибка выбора\n")


if __name__ == "__main__":
    menu()