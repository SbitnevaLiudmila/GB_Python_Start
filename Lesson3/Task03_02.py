"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def person_info(name, surname, birth_year, city, email, num_tel):

    print(name, surname, birth_year, city, email, num_tel)

person_info(name = 'Dasha', city = 'Riga', surname = 'Petrova', birth_year = 1990, email = 'dashapetrova@yandex.ru', num_tel = 7292826)