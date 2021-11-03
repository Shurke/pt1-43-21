"""
 Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
 кратных 3 пишет Fizz, вместо чисел кратный 5
 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        if i % 3 == 0:
            print('Fizz')
            continue
        if i % 5 == 0:
            print('Buzz')
            continue
        print(i)


main()
