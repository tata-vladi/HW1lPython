import math

def square(side):
    area = side ** 2
    return math.ceil(area)

side = int(input("Введите число: "))
print(square(side))


