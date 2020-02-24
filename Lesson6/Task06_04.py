"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')

class TownCar(Car):

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')
        if int(self.speed) > 60:
            print('Превышение допустимой скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')
        if int(self.speed) > 40:
            print('Превышение допустимой скорости!')

class PoliceCar(Car):
    pass


car_1 = TownCar(70, 'white', 'Mazda', False)
print(car_1.name)
print(car_1.color)
print(car_1.speed)
print(car_1.is_police)
car_1.go()
car_1.stop()
car_1.turn('направо')
car_1.show_speed()
print('\n')

car_2 = SportCar(100, 'red', 'Ferrari', False)
print(car_2.name)
print(car_2.color)
print(car_2.speed)
print(car_2.is_police)
car_2.go()
car_2.stop()
car_2.turn('налево')
car_2.show_speed()
print('\n')

car_3 = WorkCar(50, 'yellow', 'Suzuki', False)
print(car_3.name)
print(car_3.color)
print(car_3.speed)
print(car_3.is_police)
car_3.go()
car_3.stop()
car_3.turn('направо')
car_3.show_speed()
print('\n')

car_4 = PoliceCar(80, 'white', 'Ford', True)
print(car_4.name)
print(car_4.color)
print(car_4.speed)
print(car_4.is_police)
car_4.go()
car_4.stop()
car_4.turn('налево')
car_4.show_speed()