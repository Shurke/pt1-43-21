list1 = [[0], [1]]
b = 5
for i in range(1, b):
    list1 = list([*x, y] for x in list1 for y in [0, 1])

for i in list1:
    print(i)