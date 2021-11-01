"""
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

a = list(range(1, 101))
b = []
for i in a:
    if i % 3 == 0 and i % 5 == 0:
        b.append('FizzBuzz')
    elif i % 3 == 0:
        b.append('Fizz')
    elif i % 5 == 0:
        b.append('Buzz')
    else:
        b.append(i)
print(b)
