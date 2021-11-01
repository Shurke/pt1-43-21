a = input('введите предложение' )
b = a.replace(' ','')
n = ''

for i in b:
    if i not in n:
        n = n + i

print(n)
