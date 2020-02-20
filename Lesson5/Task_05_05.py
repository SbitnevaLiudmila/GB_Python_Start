"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

f = open('num_list.txt', 'w+')
f.write('30 50 49 21 98 65 5 3 2')

f = open('num_list.txt', 'r')
num_str = f.readline()
num_list = num_str.split()
sum_numbers = sum(map(int, num_list))
print(f'Сумма чисел = {sum_numbers}')

f.close

#или можно в цикле
#sum_numbers = 0
#for i in num_list:
    #i = int(i)
    #sum_numbers += i