"""Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, 
в котором они встречаются в списке."""


a = ['a','b','b','c','d','e','a']
b = []

for n in a:
    if a.count(n) == 1:
        b = b + [n]

print (b)
