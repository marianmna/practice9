x = int(input('Введите натуральное число:'))
k1 = 0
for i in range(0, 100):
    for b in range(0, 100):
        if i2 + b2 == x:
            k1 += 1
            if i != b:
                k = k1-1
            else:
                k = k1
print(k)
