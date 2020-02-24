# Author Aponasevich Ivan
# Задание 3

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

Number = int(input("Введите номер месяца: "))
if Number <= 12 and Number >= 1:
    Month_List = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    Month_Dict = dict(enumerate(Month_List))
    print(Month_Dict)

if Number == 1 or 2 or 12:
    print ('Зима')
elif Number == 3 or 4 or 5:
    print ('Весна')
elif Number == 6 or 7 or 8:
    print ('Лето')
elif Number == 9 or 10 or 11:
    print ('Осень')
else:
    print ('Error')
