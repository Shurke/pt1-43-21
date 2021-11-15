"""Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""


for int_elem in range(1, 101):
    if int_elem % 3 == 0 and int_elem % 5 == 0:
        print("FizzBuzz")
    elif int_elem % 3 == 0:
        print("Fizz")
    elif int_elem % 5 == 0:
        print("Buzz")
    else:
        print(int_elem)
