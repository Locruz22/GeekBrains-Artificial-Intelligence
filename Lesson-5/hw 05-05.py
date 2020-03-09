# Author Aponasevich Ivan
# Задание 5
#
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def sum_numbers():
    try:
        with open('File_for_hw5.txt', 'w+') as file:
            i = input('Введите цифры разделяя их пробелом: ')
            file.writelines(i)
            numb = i.split()
            print(sum(map(int, numb)))
    except ValueError:
        print('Ошибка ввода-вывода')


sum_numbers()
