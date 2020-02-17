"""Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

from itertools import count, cycle

for el in count(43):
    if el > 200:
        break
    else:
        print(el)


c = 0
for el in cycle('python'):
    if c > 50:
        break
    else:
        c += 1




#print('\n', el)
