"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

f = open('second.txt', 'w+')        #уже лень не программно создавать, можно программно? :)
f.write('первая fgh строка' + '\n')
f.write('вторая строка' + '\n')
f.write('третья строка' + '\n')
f.write('четвертая строка' + '\n')
f.write('пятая строка' + '\n')
f.write('шестая строка' + '\n')

f = open('second.txt', 'r')
print(len(f.readlines()))           #способ 1 (.readlines считывает каждую строку в массив списков)


f.seek(0)                           #возврат указателя
count_lines = 0                     # способ 2, в цикле
for line in f:
    count_lines += 1                # указатель надо возвращать в начало, иначе неправильно считает
print(count_lines)


f.seek(0)                       # возврат указателя в начало
count = sum(1 for line in f)    #способ 3, нашла в интернете, интересно, каждый перебор добавляет единицу в сумму
print(count)

f.seek(0)                   # возврат указателя в начало   #считаем все в цикле: и строки и слова, enumerate - удобно
total_lines = 0             #как вывести в одну строку, без переноса???
for line_no, line in enumerate(f, start=1):
    total_lines += 1
    print(f'количество слов в строке {line_no} "{line}" равно {len(line.split())} ')

print(f'Количество строк: {total_lines}')

f.close