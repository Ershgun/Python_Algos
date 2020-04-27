"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'
"""

P = int(input('Сколько будет чисел? - '))
N = int(input('Какую цифру считать? - '))
I = 1
nums = 0
while P > 0:
    T = int(input(f'Число №{I}: '))
    while T != 0:
        num = T % 10
        if num == N:
            nums += 1
        T //= 10
    I += 1
    P -= 1
print(f"Было введено {nums}-цифр(а)(ы) под номером '{N}'")
