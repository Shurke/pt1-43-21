"""Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого 
элемента не было."""


lst1 = [a + b for a in 'ab' for b in 'bcd']

print(lst1)
lst2 = lst1[::2]

print(lst2)
lst3 = [str(i) + 'a' for i in range(1, 5)]

print(lst3)
print(lst3.pop(1))
import copy
lst4 = copy.deepcopy(lst3)
lst5 = ['2a']

print(lst4 + lst5)
