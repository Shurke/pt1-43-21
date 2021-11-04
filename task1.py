m = int(input('цена рублей'))
n = int(input('коппеек'))
s = int(input('колл. товара'))

print((m * s + n * s // 100), (n * s % 100))
