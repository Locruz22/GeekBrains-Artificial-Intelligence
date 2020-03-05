# Author Aponasevich Ivan
# Задание 5
#
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(el_p, el):
    return el_p * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
new_list = reduce(my_func, my_list)

print(my_list)
print(new_list)
