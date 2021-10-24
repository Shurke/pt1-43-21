a = int(input('a = '))
d = a
b = 0
c = 0
while d > 0:
    b = b * 10 + d % 10
    d = d // 10
if a == b:
    print('Да, является')
else:
    print('Не является')
