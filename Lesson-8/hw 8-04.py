# Author Aponasevich Ivan
# Задание 4
#
"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class OrgTech:
    def __init__(self, name, price, count_of_products, lists_number):
        self.name = name
        self.price = price
        self.quantity = count_of_products
        self.lists = lists_number


class Printer(OrgTech):
    def to_print(self):
        return f'Распечатанно {self.lists} раз'


class Scanner(OrgTech):
    def to_scan(self):
        return f'Отсканированно {self.lists} раз'


class Xerox(OrgTech):
    def to_copier(self):
        return f'Откесрокопированно  {self.lists} раз'


printer = Printer('Canon', 2000, 40, 20)
scanner = Scanner('Epson', 1200, 14, 20)
xerox = Xerox('Xerox550', 1500, 5, 10)


print(printer.to_print())
print(scanner.to_scan())
print(xerox.to_copier())