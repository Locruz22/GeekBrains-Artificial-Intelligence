# Author Aponasevich Ivan
# Задание 1
#
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    lines = input("Введите данные: ")
    if lines == '':
        print(my_list)
        break
    else:
        lines_2 = lines + '\n'
        my_list.append(lines_2)

with open("TextFile_hw1.txt", "w") as file:
    file.writelines(my_list)