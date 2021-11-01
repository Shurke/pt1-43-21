a = int(input('введите число: '))
a1 = a
pol = 0

while a1 > 0:
    b = a1 % 10
    a1 = a1 // 10
    pol = pol * 10
    pol = pol + b

if a == pol:
    print('полиндром')
else:
    print('не полиндром') 
