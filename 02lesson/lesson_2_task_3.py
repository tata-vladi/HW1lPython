import math

def square(side):
    area = side ** 2
    return math.ceil(area)

side = float(input("Введите число: "))
print(square(side))


