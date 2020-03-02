"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""


my_raiting = [7, 5, 3, 3, 2]

num = int(input('введите число '))

for i in range(len(my_raiting)):
    if num >= my_raiting[i]:
        my_raiting.insert(i, num)
        break
else:
    my_raiting.append(num)

print(my_raiting) #проверка

my_raiting = [7, 5, 3, 3, 2]

num = int(input('введите число '))

for i in range(len(my_raiting)):
    if num >= my_raiting[i]:
        my_raiting.insert(i, num)
        break
else:
    my_raiting.append(num)

print(my_raiting) #проверка


# эти комменты для меня, они неверные
# if num in my_raiting:
    #place = my_raiting.index(num)
    #my_raiting.insert(place + 1, num)
#elif num > my_raiting[0]:
    #my_raiting.insert(0, num)
#elif num < my_raiting[-1]:
    #my_raiting.append(num)
#else

#for i in my_raiting[:]:
    #if num >= i:
        #place = my_raiting.index(i)
        #print(place)
        #my_raiting.insert(place, num)
        #break
    #else:
        #my_raiting.append(num)
        #break

#print(my_raiting)

    #place = my_raiting.index(num)
    #my_raiting.insert(place, num)
    #print(plac_e)

my_raiting = [7, 5, 3, 3, 2]

num = int(input('введите число '))

for i in range(len(my_raiting[:])):
    if num >= my_raiting[i]:
        my_raiting.insert(i, num)
        print(my_raiting)
        break
else:
    my_raiting.append(num)
    print(my_raiting)

#if num in my_raiting:
    #place = my_raiting.index(num)
    #my_raiting.insert(place + 1, num)
#elif num > my_raiting[0]:
    #my_raiting.insert(0, num)
#elif num < my_raiting[-1]:
    #my_raiting.append(num)
#else

"""for i in my_raiting[:]:
    if num >= i:
        place = my_raiting.index(i)
        print(place)
        my_raiting.insert(place, num)
        break
    else:
        my_raiting.append(num)
        break

print(my_raiting)"""

# Катя сделала
n = int(input())
rating = []
for i in range(n):
    new = int(input())
    j = 0
    while j < len(rating) and rating[j] > new:
        j += 1
    rating.insert(j, new)
print(*rating)