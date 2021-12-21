"""
Задача 8 из 'Проекта Эйлера'

Найдите наибольшее произведение тринадцати
последовательных цифр в данном числе.

Пример:
input:
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

output:
23514624000

Для расширения функционала была добавлена опция
выбора количества последовательных цифр
"""
import string


def converting_to_list(str_number: str) -> list:
    """converts string to list"""
    ans_list = []
    for digit in str_number.replace('\n', ''):
        if digit not in string.digits:
            raise ValueError('Wrong Input data')
        ans_list.append(int(digit))
    return ans_list


def max_product(input_num: str, multipliers: int) -> int:
    """returns maximum product of 'multipliers' digits in row"""

    # checks if input_list is not a 'list' type
    if not isinstance(input_num, str):
        raise ValueError('list expected, got -', type(input_num))
    # checks if 'multipliers' argument is not an 'int' type
    if not isinstance(multipliers, int):
        raise ValueError('expected int argument, got -', type(multipliers))
    # checks if number of multipliers is less than 1
    if multipliers < 1:
        raise ValueError('number of multipliers should be positive')

    input_num = converting_to_list(input_num)
    max_product_ans = 0
    for digit in range(len(input_num) - multipliers + 1):
        curr_product = 1
        for digit_ in range(digit, digit + multipliers):
            curr_product *= input_num[digit_]
        max_product_ans = max(max_product_ans, curr_product)
    return max_product_ans
