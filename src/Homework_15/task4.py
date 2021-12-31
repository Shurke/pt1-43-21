"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества
чисел, меньших n, которые взаимно просты с n. К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и
взаимно просты с девятью, φ(9)=6.
n 	Взаимно простые числа 	φ(n) 	n/φ(n)
2 	1 	                    1   	2
3 	1,2 	                2 	    1.5
4 	1,3 	                2 	    2
5 	1,2,3,4 	            4 	    1.25
6 	1,5 	                2 	    3
7 	1,2,3,4,5,6 	        6 	    1.1666...
8 	1,3,5,7 	            4 	    2
9 	1,2,4,5,7,8 	        6 	    1.5
10 	1,3,7,9 	            4 	    2.5

Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.
Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.

WARNING: for values 'n' from 1 to 1kk, the function is performed for a long time (~20min)!
The numba module worked for speed up processing function.
"""


from numba import njit


@njit()
def euler(num: int) -> float:
    """Euler's function takes a natural number as input and outputs the ratio of number to the

    number of co-prime numbers.
    """
    total_num = num
    prime_number: int = 2
    num_of_co_prime_numbers: int = 1
    count: int = 0
    while True:
        if num % prime_number == 0:
            count += 1
            num /= prime_number
            if count == 1:
                num_of_co_prime_numbers *= prime_number - 1
            elif count > 1:
                num_of_co_prime_numbers *= prime_number
        else:
            prime_number += 1
            count = 0
        if prime_number > num:
            break
    return total_num / num_of_co_prime_numbers


def max_euler(num: int = None) -> tuple:
    """The function iterate numbers from range , processing it with Euler func

    and return the maximum value
    """
    if num is None:
        num = int(input('For processing nums from 1 to "n", enter "n": '))
    if type(num).__name__ != 'int':
        raise TypeError('Please enter a simple integer!')
    max_of_euler_func: tuple = 0, 0
    for element in range(1, num + 1):
        result: float = euler(element)
        if result > max_of_euler_func[1]:
            max_of_euler_func = element, result
    return max_of_euler_func
