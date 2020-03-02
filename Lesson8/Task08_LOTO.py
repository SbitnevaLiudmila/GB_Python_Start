from random import sample
import sys
import time

class Card:
    def __init__(self):
        self.num = sample(range(1, 91), k=15)
        self.line1 = self.num[:5]
        self.line1.sort()
        self.line2 = self.num[5:10]
        self.line2.sort()
        self.line3 = self.num[10:]
        self.line3.sort()
        self.crossed = dict()
        self.left = 15
        for x in self.num:
            self.crossed[x] = False

    def cross(self, x):
        if x in self.num:
            self.crossed[x] = True
            self.left -= 1
            return True
        else:
            return False

    def check(self, x):
        return '{:2}'.format(x) if not self.crossed[x] else ' -'

    def __str__(self):
        s = '-' * 26 + '\n'
        s += ' ' * 3 + self.check(self.line1[0]) + ' ' + self.check(self.line1[1]) + ' ' + self.check(self.line1[2]) + ' ' * 10 + self.check(self.line1[3]) + ' ' + self.check(self.line1[4]) + '\n'
        s += self.check(self.line2[0]) + ' ' * 4 + self.check(self.line2[1]) + ' ' * 4 + self.check(self.line2[2]) + ' ' + self.check(self.line2[3]) + ' ' * 4 + self.check(self.line2[4]) + '\n'
        s += ' ' * 3 + self.check(self.line3[0]) + ' ' + self.check(self.line3[1]) + ' ' + self.check(self.line3[2]) + ' ' * 4 + self.check(self.line3[3]) + ' ' * 4 + self.check(self.line3[4]) + '\n'
        s += '-' * 26
        return s


barrels = sample(range(1, 91), k=90)
print(barrels)
player_card = Card()
computer_card = Card()
for i in range(90):
    print('Новый бочонок:', barrels[i], '(осталось {})'.format(90 - i - 1))
    print('Ваша карточка:', player_card, sep='\n')
    print('Карточка компьютера', computer_card, sep='\n')
    print('Зачеркнуть цифру? (y/n)')
    comm = input()
    if comm == 'y':
        res = player_card.cross(barrels[i])
        if not res:
            print('Вы проиграли')
            break
    else:
        if barrels[i] in player_card.num:
            print('Вы проиграли')
            break
    if barrels[i] in computer_card.num:
        computer_card.cross(barrels[i])
    if player_card.left == 0 and computer_card.left != 0:
        print('Вы выиграли!')
        break
    elif player_card.left == 0:
        print('Игра окончилась вничью')
        break
    elif computer_card.left == 0:
        print('Вы проиграли')
        break