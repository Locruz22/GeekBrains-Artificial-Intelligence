# Author Aponasevich Ivan
# Задание 4
#
""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. """


class Car:
    # Методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Аттрибуты
    def go(self):
        print("{} машина поехала!".format(self.name))

    def stop(self):
        print("{} машина остановилась.".format(self.name))

    def turn(self, direction):
        print("{} машина повернула {}".format(self.name, direction))

    def show_speed(self):
        print("Скорость: {}".format(self.speed))


# дочерние классы

class TownCar(Car):
    def limit_speed_TownCar(self):
        if self.speed > 60:
            print("Превышена скорость")
        else:
            print("Скорость {}".format(self.speed))


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def limit_speed_WorkCar(self):
        if self.speed > 40:
            print("Превышена скорость!")
        else:
            print(f"Скорость {self.name} {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} – полицейская машина"
        else:
            return f"{self.name} – полицейская машина"


ford = WorkCar(77, 'Черная', 'Ford', False)
audi = SportCar(150, 'Малиновая', 'Audi', False)
chevrolet = PoliceCar(70, 'Синяя', 'Chevrolet', True)
volkswagen = TownCar(61, 'Зеленая', 'Volkswagen', False)

print(f'Машина {volkswagen.name} – {volkswagen.color}')

print(f'{audi.name} – полицейская машина?')
if audi.is_police is True:
    print("Да, она полицейская")
else:
    print("Нет, она не полицейская")

print(f'{chevrolet.name} – полицейская машина?')
if chevrolet.is_police is True:
    print("Да, она полицейская")
else:
    print("Нет, она не полицейская")
print(audi.show_speed())
print(ford.show_speed())
