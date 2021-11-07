a = str(input('Введите предложение', ))
am = 0
ab = 0

for i in a:
    if i.islower():
        am += 1
    else:
        ab += 1

print('больших', ab)
print('маленьких', am)
