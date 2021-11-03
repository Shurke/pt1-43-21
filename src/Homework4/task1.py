"""
FizzBuzz

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

for i in range(100):
    p = i + 1
    if p % 3 == 0 and p % 5 == 0:
        print('FizzBuzz')
    elif p % 3 == 0:
        print('Fizz')
    elif p % 5 == 0:
        print('Buzz')
    else:
        print(p)
