"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for row in self.matrix_list:
            print(*row, end="\n")
        return ''

    def __add__(self, other):
        matrix_sum = []
        for y in zip(self.matrix_list, other.matrix_list):
            my_list = []
            for x in zip(*y):
                my_list.append(sum(x))
            matrix_sum.append(my_list)
        return Matrix(matrix_sum)


m = Matrix([[31, 22, 11], [37, 43, 1], [51, 86, 77]])
print(m)
m1 = Matrix([[37, 40, 99], [100, 45, 17], [501, 6, 77]])
print(m + m1)

# второй вариант печати матрицы

    #def __str__(self):
        #for row in self.my_list:
            #for i in row:
                #print(f"{i:4}", end="") # '4 - это размер поля те 4 символа и склейка в строку, а не новый столбец
            #print()
        #return ''


# сложение матрицы поэлементно
    #def __add__(self, other):
        #for x in range(len(self.matrix_list)):
            #for y in range(len(self.matrix_list[0])):
            #self.matrix_list[x][y] = self.matrix_list[x][y] + other.matrix_list[x][y]
        #return self.matrix_list  # Matrix.__str__(self)


#m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
#new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
#print(m + new_m)
#print(m.__add__(new_m))

# ниже через zip еще вариант
        #result = [[sum(x) for x in zip(*y)] for y in zip(self.matrix_list, other)]

#def __add__(self, other):
        #result = []
        #numbers = []
        #for i in range(len(self.a)):
            #for j in range(len(self.a[0])):
                #summa = other.a[i][j] + self.a[i][j]
                #numbers.append(summa)
                #if len(numbers) == len(self.a):
                    #result.append(numbers)
                    #numbers = []
        #return Matrix(result)

#def __str__(self):
        #for row in self.matrix_list:
            #return '\n'.join(map(str, self.matrix_list))  # выводит в квадратных скобках, не пойдет

    #def __str__(self):
        #return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix_list]))

    #print(f"{i:4}", end="")  4 - это длина поля

#def __str__(self):
    #for row in self.matrix_list:
        #for i in row:
            #print(f'{i}', end='\t')
        #print()
    #return ''


#рабочий хороший вариант
    #def __add__(self, other):
        #for x in range(len(self.matrix_list)):
            #for y in range(len(self.matrix_list[0])):
                #self.matrix_list[x][y] = self.matrix_list[x][y] + other.matrix_list[x][y]
        #return Matrix(self.matrix_list)

