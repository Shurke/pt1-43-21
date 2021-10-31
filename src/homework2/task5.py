'''
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы.
n - вводится
'''

number_in_fib = int(input('Enter a number: '))
n = number_in_fib - 1
a = 1
fib_sequence = [0, 1]
fib_element = fib_sequence[1]

for a in range(number_in_fib - a):
    if a < number_in_fib - 1:
        fib_element += fib_sequence[a]
        fib_sequence.append(fib_element)

print(str(number_in_fib) + 'th Fibonacci number is - ' + str(fib_sequence[n]))
