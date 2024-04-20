for m in range(100000, 1000000):
    if str(m) == str(m)[::-1] and str(m % 100000) == str(m % 100000)[::-1] and str(m % 10000 // 10) == str(m % 10000 // 10)[::-1]:
        print("Пробег автомобиля:", m)
        break
