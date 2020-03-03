# Author Aponasevich Ivan
# Задание 1
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    mylist = [x, y, z]
    all = []
    max_1 = max(mylist)  # максимальное число в списке
    all.append(max_1)
    mylist.remove(max_1)
    max_2 = max(mylist) # второе максимальное число в списке
    all.append(max_2)
    print(sum(all))

my_func(10, -66, 20)

