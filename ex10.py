n = int(input("Введите количество кубиков N: "))

p = [0] * (n + 1)
p[0] = 1

for i in range(1, n + 1):
    for j in range(i):
        p[i] += p[j]

print(p[n])
