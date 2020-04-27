"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import randint

N = randint(0, 100)
P = 1
S = 10
print('Угадайте число от 0 до 100.\nУ вас 10 попыток')
while P <= S:
    T = int(input(f'Угадывайте число: '))
    if N == T:
        print(f'Вы угадали c {P} попытки!')
    elif T < N:
        if P < S:
            print(f'Вы указали МЕНЬШЕЕ число, у вас осталось {S - P} попыток')
        else:
            print('вы проиграли')
    elif T > N:
        if P < S:
            print(f'Вы указали БОЛЬШОЕ число, у вас осталось {S - P} попыток')
        else:
            print('вы проиграли')
    P += 1
print(f'Загаданное число: {N}')
