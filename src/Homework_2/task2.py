"""    2. List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было."""

lst = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]

print(lst)
