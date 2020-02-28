# Author Aponasevich Ivan
# Задание 1

# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

MyTuple = (12, "Ho-ho-ho", 333, 9)
MyList = ['Hello!', 2321, 2.2, True]
MyStr = "Abrakadabra"
MyDictionary = {'MyHeight': '185', 'MyWeight': '72'}
MainList = [MyTuple, MyList, MyStr, MyDictionary]

for i in MainList:
    print(f'{i} is {type(i)}')
