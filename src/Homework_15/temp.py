from time import time

start_time = time()
def euler(num):
    """Euler's function takes a natural number as input and outputs the number of
    coprime numbers
    :param num: natural number
    :return: the coprime numbers"""
    prime_number = 2
    result = 1
    count = 0
    while True:
        if num % prime_number == 0:
            count += 1
            num /= prime_number
            if count == 1:
                result *= prime_number - 1
            elif count > 1:
                result *= prime_number
        else:
            prime_number += 1
            count = 0
        if prime_number > num:
            break
    return result

def task4(n: int) -> tuple:

    """Function for iteration start.
    :param n:
    :param collection: iterable object must be 'list' or 'tuple', or one number 'int' type
    :return: the maximum ratio of 'n' to the Euler(n) function"""
    max_value = 0, 0

    for i in range(1, n + 1):
        result = i / euler(i)
        if result > max_value[1]:
            max_value = i, result
        # task4.cache_clear()
    return max_value

print(task4(100000))
print(5 * '*', 'time: ', time() - start_time, 5 * '*')