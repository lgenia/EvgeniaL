import math


def square(a, b):
    return math.ceil(a*b)


a = float(input('Введите первую строну: '))
b = float(input('Введите вторую сторону: '))


print(f'Округленная в большую сторону сумма - {square(a, b)}')
