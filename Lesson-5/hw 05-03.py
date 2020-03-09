# Author Aponasevich Ivan
# Задание 3
#
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


Staff = {'Reeves': 170000, 'Goddard': 21000, 'Anderson': 19999, 'Viki': 15001,
         'Nicholson': 12999, 'Freeman': 14000, 'Spoke': 34000, 'Smith': 44000}
try:
    fileS = open("Staff.txt", 'w')
    for ln, salary in Staff.items():
        fileS.write(ln + ':' + str(salary) + "\n")
except IOError:
    print("Ошибка ввода-вывода!")
finally:
    fileS.close()
sum = 0
count = 0
people = []
with open("Staff.txt", "r") as fileS:
    for line in fileS:
        print(line, end="")
        rub = line.split(':')
        if int(rub[1]) <= 20000:
            people.append(rub[0])
        sum += int(rub[1])
        count += 1
result = sum / count
print(f"Всего людей с окладом менее 20 000: {people}")
print(f"Средняя зарплата: {result}")
