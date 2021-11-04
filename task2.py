a = str(input(' введите предложение'))
a = a.replace(',', ' ')
a = a.replace('.', ' ')
b = a.split(' ')
c = 0
res = 0

for i in b:
    if len(i) > c:
        c = len(i)
        res = i

print(res)
