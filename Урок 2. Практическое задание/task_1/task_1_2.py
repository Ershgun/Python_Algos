"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def rec(sign):
    if sign == '0':
        print('\nДо свидания!\nРабота программы завершена.')
        sing == 0
        return
    else:
        if sign in ('+', '-', '*', '/'):
            try:
                A = int(input('Введите первое число:'))
                B = int(input('Введите второе число:'))
            except ValueError:
                print('Это не число.')
            else:
                if sign == '+':
                    print(f'Ваш результат: {A} + {B} = {A + B}')
                elif sign == '-':
                    print(f'Ваш результат: {A} - {B} = {A - B}')
                elif sign == '*':
                    print(f'Ваш результат: {A} * {B} = {A * B}')
                elif sign == '/':
                    if B != 0:
                        print(f'Ваш результат: {A} / {B} = {A / B}')
                    else:
                        print('На ноль делить нельзя! Введите другие числа.')
        else:
            print('Вы ввели недопустимый символ!')

        rec(input('Введите операцию (+, -, *, / или 0 для выхода):'))
        return

sing = input('Введите операцию (+, -, *, / или 0 для выхода):')
rec(sing)
