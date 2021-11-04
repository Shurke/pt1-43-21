"""
Напишите программу, которая печатает цифры от 1 до 100, 
но вместо чисел, кратных 3 пишет Fizz, 
вместо чисел кратный 5 пишет Buzz, 
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def main():
    for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz", end=' ')
    elif x % 3 == 0:
        print("Fizz", end=' ')
    elif x % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(x, end=' ')


if __name__ == "__main__":
    main()
