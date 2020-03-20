# Author Aponasevich Ivan
# Задание 1
#
""" Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление
значения до целого числа.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида **\n\n***..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 **\n\n. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
 строку: **\n\n***. """


class Cell:
    def __init__(self, count):
        self.count = int(count)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.count // rows)]) + '\n' + '*' * (self.count % rows)

    # добавление клеток
    def __add__(self, other):
        return 'Sum of cells ' + str(self.count + other.count)

    # вычитание клеток
    def __sub__(self, other):
        return (self.count - other.count) if (self.count - other.count) > 0 else print('Нет клеток')

    # умножение
    def __mul__(self, other):
        return 'Multiply of sells ' + str(self.count * other.count)

    # деление (округляет до целого числа)
    def __truediv__(self, other):
        return 'Div of cells ' + round(self.count / other.count)


cell_0 = Cell(10)
cell_1 = Cell(2)
cell_2 = Cell(-5)
print(cell_0 + cell_1)
print(cell_0 / cell_1)
print(cell_1 + cell_2)
print(cell_0.make_order(99))
