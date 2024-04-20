N = int(input('Введите число веревок,выданное команде:'))
k=0
while N>0:
    N = int(input('Введите число веревок,выданное команде:'))
    if N==0:
         break
    else:
        if N%4==0:
            k+=1
print(k)
