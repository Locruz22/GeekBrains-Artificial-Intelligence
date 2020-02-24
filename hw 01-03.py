# Author Aponasevich Ivan
# Задание 3

#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите число: ")
a = int(n+n)
b = int(n+n+n)
sum = int(n) + a + b
print(sum)
