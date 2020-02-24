"""Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""
import time
import itertools


class Trafficlight:
    def __init__(self, colors):
        self.__colors = colors

    def running(self):
        for color in itertools.cycle(self.__colors):
            print(color, end=' ')
            if color == 'red':
                time.sleep(7)
            elif color == 'yellow':
                time.sleep(2)
            elif color == 'green':
                time.sleep(6)


a = input('Введите цвета через пробел: ').split()
if a != ['red', 'yellow', 'green'] and a != ['yellow', 'green', 'red'] and a != ['green', 'red', 'yellow']:
    print('Неверные цвета!')
else:
    my_trafficlight = Trafficlight(a)
    my_trafficlight.running()
