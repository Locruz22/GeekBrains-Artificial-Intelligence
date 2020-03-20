# Author Aponasevich Ivan
# Задание 1
#
""" Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property. """


class Wear:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_coat(self):
        return self.width / 6.5 + 0.5

    def square_suits(self):
        return self.height * 2 + 0.3

    @property
    def sq_all(self):
        return str(f'Площадь ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Wear):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто: {self.square_c}'


class Suits(Wear):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм: {self.square_j}'


coat = Coat(23, 34)
jacket = Suits(11, 19)
print(coat)
print(jacket)
print(coat.sq_all)
print(jacket.sq_all)
