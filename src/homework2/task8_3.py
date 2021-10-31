'''
Task 3
A square of squares
Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")
'''

def is_square(n):
    if n >= 0:
        if n ** 0.5 % 1 == 0:
            return True
        else:
            return False
    else:
        return False

print('Task3 result')
print(is_square(3))
print(is_square(26))
print(is_square(25))

