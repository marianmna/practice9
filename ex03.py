N = int(input('Введите кол-во упаковок эскимо:'))
min = 1000
for i in range(2, 1000):
    if N % i == 0 and N % i < i < min:
        min = i
        print(i)
