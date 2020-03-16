# Author Aponasevich Ivan
# Задание 3
#
""" Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage = income['wage']
        self.income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self.income_bonus + self.income_wage)


emp = Position('Froddo', 'Baggins', 'Traveller', {"wage": 100000, "bonus": 50000})
emp.get_full_name()
emp.get_total_income()