N = int(input("Введите наибольшее количество точек на одной плитке кости домино: "))
summa = 0

for i in range(N+1):
    for j in range(i+1):
        summa += i + j

print("Суммарное количество точек на всех костях домино:", summa)
