"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""

A = int(input("Введите количество чисел: "))
step = 0
max = 0
I = 1
for k in range(0, A):
    number = input(f"Введите число: № {I} ")
    sum = 0
    for i in number:
        sum += int(i)
    if sum > max:
        max = sum
        max_num = number
    I += 1
step += 1
print(f"Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max}")
