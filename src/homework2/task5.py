'''
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы.
n - вводится
'''

number_in_fib = int(input('Enter a number: '))

if 2 <= number_in_fib <= 3:
    fib_element = 1
elif number_in_fib == 1:
    fib_element = 0
else:
    fib_element = 2
    fib_element_left = 1
    for element in range(3, number_in_fib):
        fib_element_left, fib_element = fib_element, fib_element_left + fib_element

print(str(number_in_fib) + 'th Fibonacci number is - ' + str(fib_element))
