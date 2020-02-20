"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

f = open('numbers.txt', 'w+')
f.write('One — 1' + '\n')
f.write('Two — 2' + '\n')
f.write('Three — 3' + '\n')
f.write('Four — 4' + '\n')

russian_numbers = {'1':'Один', '2':'Два', '3':'Три', '4':'Четыре'}

f = open('numbers.txt', 'r')

my_list = f.readlines()

rus_string_list = []
for item in my_list:
    new_item_list = item.strip().split()            #new_item = item.strip() new_item_list = new_item.split()
    for key, value in russian_numbers.items():
        if key == new_item_list[-1]:
            new_item_list[-1] = value
            rus_string = ' '.join(new_item_list)
            rus_string_list.append(rus_string)

rus_string_list = '\n'.join(rus_string_list)
print(rus_string_list)

new_f = open('russian_numbers.txt', 'w+')

new_f.write(rus_string_list)

f.close
new_f.close


