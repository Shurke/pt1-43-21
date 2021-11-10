"""
FizzBuzz

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print('FizzBuzz')
    elif item % 3 == 0:
        print('Fizz')
    elif item % 5 == 0:
        print('Buzz')
    else:
        print(item)
