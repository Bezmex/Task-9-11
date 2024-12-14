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
        menu_choice = input("Выберите пункт для дальнейшей работы: ")
        if is_int(menu_choice):
            menu_choice = int(menu_choice)

        if menu_choice == 1:
            show_tasks()
            task_choice = input("Введите номер выбранной задачи: ")
            is_task_selected = True

        elif menu_choice == 2:
            if is_task_selected:
                print("Введите данные...")
                is_info_input = True
            else:
                print("\nСначала выберите задание\n")

        elif menu_choice == 3:
            if is_task_selected and is_info_input:
                print("Выполнение алгоритма")
                is_algoritm_done = True
            else:
                print("\nСначала введите данные для выполнения алгоритма\n")

        elif menu_choice == 4:
            if is_algoritm_done:
                print("Результат работы алгоритма")
            else:
                print("\nСначала выполните алгоритм\n")

        elif menu_choice == 5:
            break
        else:
            print("\nОшибка выбора\n")


if __name__ == "__main__":
    menu()
