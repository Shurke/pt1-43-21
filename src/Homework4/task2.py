"""
List practice

1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.
"""

list_gener = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]
print(list_gener)
print(list_gener[::2])
list_gener = [str(i + 1) + 'a' for i in range(4)]
print(list_gener)
list_gener.remove('2a')
print(list_gener)
list_gener_new = list_gener.copy()
list_gener_new.append('2a')
print(list_gener_new, list_gener)
