import math


def square(length):
    return math.ceil(length)


lenght = int(input('Введите длину стороны: '))
print('Площадь квадрата = ', lenght*lenght)
