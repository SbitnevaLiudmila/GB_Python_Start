"""Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

import re

f = open('subject.txt', 'r')
subject_list = []
sum_hours_list = []
for line in f:
    my_list = re.split(':', line)         #делим строку по двоеточию, чтобы вытащить название предмета
    subject = my_list.pop(0)
    subject_list.append(subject)
    hours_list = re.findall(r'\d+', line)        #выбираем цифры
    sum_hours = sum(map(int, hours_list))
    sum_hours_list.append(sum_hours)

subject_dict = dict(zip(subject_list, sum_hours_list))

print(subject_dict)

f.close

#[int(num) for num in my_str.split() if num.isdigit()] так еще можно вытащить числа
