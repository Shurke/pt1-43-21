a = 1
b = 1
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
i = 0

while i < n - 2:
    c = a + b
    a = b
    b = c
    i = i + 1

print("Значение этого элемента:" , b)
