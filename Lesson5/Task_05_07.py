"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

with open('firms.txt', 'r') as f:
    firm_list = []
    result_list = []
    sum_fin_result = 0
    count = 0
    for line in f:
        if len(line) < 4: # проверка на пустые строки в конце
            continue
        my_list = line.split()
        if my_list[-1].isdigit() == False: continue    #чтобы не обрабатывалась первая строка с названиями столбцов
        firm = my_list[0]
        firm_list.append(firm)
        fin_result = int(my_list[-2]) - int(my_list[-1])
        result_list.append(fin_result)
        if fin_result >= 0:
            print(f'Прибыль {firm} равна {fin_result}')
            sum_fin_result += fin_result
            count += 1
        else:
            print(f'{firm} отработала с убытком {fin_result}')

    average_profit = sum_fin_result / count
    firm_dict = dict(zip(firm_list, result_list))
    average_dict = {'average_profit': average_profit}
    total_list = [firm_dict, average_dict]
    print(total_list)

import json
with open('data.json', 'w') as f:
    json.dump(total_list, f)

