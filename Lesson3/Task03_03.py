"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(num_1, num_2, num_3):
    result = sum([num_1, num_2, num_3]) - min([num_1, num_2, num_3])
    return result

print(my_func(3, 7, 5))