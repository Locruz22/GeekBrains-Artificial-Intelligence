# Author Aponasevich Ivan
# Задание 2
#
"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой. """


class DivisionByNull:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.denominator = dividend

    @staticmethod
    def divide_by_null(divider, dividend):
        try:
            return divider / dividend
        except:
            return f"Нельзя делить на ноль!"


div = DivisionByNull(2, 30)
print(DivisionByNull.divide_by_null(30, 0))
print(DivisionByNull.divide_by_null(100, 0.1))
print(DivisionByNull.divide_by_null(100, True))
print(div.divide_by_null(1000, 0))
