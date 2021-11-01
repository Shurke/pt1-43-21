""" Условие задачи 1, FizzBuzz

    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

for number in range(1, 101):
    divisible3 = number % 3 == 0
    divisible5 = number % 5 == 0
    if divisible3 and divisible5:
        print("FizzBuzz")
    elif divisible3:
        print("Fizz")
    elif divisible5:
        print("Buzz")
    else:
        print(number)
