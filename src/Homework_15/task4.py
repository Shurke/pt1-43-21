"""
WARNING: for values 'n' from 1 to 1kk, the function is performed for a long time (~20min)!
The numba module worked for speed up processing function.
"""

import time
from numba import njit


@njit()
def _euler(num: int) -> float:
    """
    Euler's function takes a natural number as input and outputs the ratio of number to the number
    of co-prime numbers.
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


def max_euler(n: int = None) -> tuple:
    """
    The function iterate numbers from range , processing it with Euler func
    and return the maximum value
    """
    if n is None:
        n = int(input('For processing nums from 1 to "n", enter "n": '))
    elif type(n).__name__ != 'int':
        raise 'Please enter a simple integer!'
    max_of_euler_func: tuple = 0, 0
    for element in range(1, n + 1):
        result: float = _euler(element)
        if result > max_of_euler_func[1]:
            max_of_euler_func = element, result
    return max_of_euler_func
