# задачи решал на codewar

"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})"""



def cakes(recipe, available):
    result = []
    try:
        for i in recipe:
            result.append(available[i] // recipe[i])
    except:
        result.append(0)
    return min(result)
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))



"""Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :)
 :D
 ;-D :~)
Invalid smiley faces: ;(
 :> :} :]


Example
countSmileys([':)
', ';(
', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(
', ':-)
', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$
', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same."""

def count_smileys(arr):
    count = 0
    for i in arr:
        if i[0] not in ':;':
            continue
        elif i[-1] not in ')D':
            continue
        elif len(i) == 3 and i[1] not in '-~':
                continue
        else:
            count += 1
    return count

print(count_smileys([';D', ':-(', ':-)', ';~)']))

""" There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance."""


def find_uniq(arr):
    set_num = set(arr)
    for i in set_num:
        if arr.count(i) == 1:
            break
    return i
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))


"""Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case"""

def count_bits(n):
    return bin(n).count('1')

print(count_bits(1234))