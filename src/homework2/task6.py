a = int(input('Попробуй ввести полиндром, Катька: '))
count = 0
lista = []
listb = []
while a > 0:
    b = (a % 10)
    lista.append(b)
    a //= 10
    count += 1

# print(count)
# print(lista)
for i in reversed(lista):
    listb.append(i)
# print(listb)
if lista == listb:
    print('It is polindrome!')
else:
    print('It is not polindrome(')
