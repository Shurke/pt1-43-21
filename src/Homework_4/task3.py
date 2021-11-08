"""
Tuple practice
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу последовательно
выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""


lst = [1, 2, 3]
tup = (lst,)

for elem in tup:
    for char in elem:
        print(char)
print("len(tup) = ", len(tup))
