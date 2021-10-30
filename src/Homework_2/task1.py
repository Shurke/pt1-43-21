"""    1. FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""

lst = [i for i in range(1, 101)]
lst_res = []

for i in lst:
    if i % 3 == 0 and i % 5 == 0:
        lst_res.append('FizzBuzz')
    elif i % 3 == 0:
        lst_res.append('Fizz')
    elif i % 5 == 0:
        lst_res.append('Buzz')
    else:
        lst_res.append(i)
print(lst_res)
