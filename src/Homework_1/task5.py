"""5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
Задачу поместите в файл task5.py в папке src/homework2."""

# последовательность наичнается с 0!
fib = 0
fib_next = 1

for i in range(int(input('Enter № of num in Fibonachi  string: ')) - 1):
    fib, fib_next = fib_next, fib_next + fib
print(fib)
