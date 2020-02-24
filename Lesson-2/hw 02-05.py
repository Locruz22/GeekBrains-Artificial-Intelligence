# Author Aponasevich Ivan
# Задание 5

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


number = int(input("Введите число: "))
main_list = [4, 1, 9, 5, 2]
a = main_list.count(number)
for element in main_list:
    if a > 0:
        i = main_list.index(number)
        main_list.insert(i + a, number)
        break
    else:
        if number > element:
            j = main_list.index(element)
            main_list.insert(j, number)
            break
        elif number < main_list[len(main_list) - 1]:
            main_list.append(number)
print(main_list)