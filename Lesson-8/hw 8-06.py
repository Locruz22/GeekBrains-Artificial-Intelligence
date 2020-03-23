# Author Aponasevich Ivan
# Задание 6
#
"""Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.

"""


class OrgTech:
    def __init__(self, name, price, count_of_products, lists_number, *args):
        self.name = name
        self.price = price
        self.count_of_products = count_of_products
        self.lists = lists_number
        self.store_is_full = []
        self.store = []
        self.product = {'Модель устройства': self.name, 'Цена за единицу товара': self.price,
                        'Количество': self.count_of_products}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.count_of_products}'

    def receiving(self):
        try:
            unit = input(f'Введите название товара: ')
            unit_p = int(input(f'Введите цену за единицу товара: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель': unit, 'Цена за единицу товара': unit_p, 'Количество': unit_q}
            self.product.update(unique)
            self.store.append(self.product)
            print(f'Текущий список -\n {self.store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.store_is_full.append(self.store)
            print(f'Весь склад -\n {self.store_is_full}')
            return f'Выход'
        else:
            return OrgTech.receiving(self)


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