from math import sqrt
n = int(input('Введите положительное число,большее 2:'))
while n > 2:
    n = sqrt(n)
    print("%.3f" % n)
