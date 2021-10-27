# Define a function that takes one integer argument and returns
# logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number
# greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive.
# You may be given negative numbers as well (or 0).

def is_prime(num):
    a = True if num > 1 else False
    for i in range(2, num - 1):
        if num % i != 0:
            a = True
        else:
            a = False
            break

    return a


print(is_prime(int(input('Enter a number: '))))
