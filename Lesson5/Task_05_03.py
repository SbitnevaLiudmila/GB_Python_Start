"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

f = open('staff.txt', 'w+')
f.write('Иванов 15000' + '\n')
f.write('Петров 27000' + '\n')
f.write('Сидоров 12000' + '\n')
f.write('Гагарин 9000' + '\n')
f.write('Кузнецов 16000' + '\n')

f = open('staff.txt')
sum_salary = 0
count = 0
for line_no, line in enumerate(f, start=1):
    new_line = line.split()
    salary = int(new_line[1])
    sum_salary += salary
    count += 1
    if salary < 20000:
        print(new_line[0])

average_salary = sum_salary / count

print(f'Средняя величина дохода сотрудников: {average_salary}')

f.close
