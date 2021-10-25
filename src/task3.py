s = input('Введите предложение: ')
s = s.replace(' ', '')
s = list(s)
new_s = ''
for n in s:
    if new_s.find(n) == -1:
        new_s = new_s + n
print(new_s)