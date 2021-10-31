'''
here is an array with some numbers.
All numbers are equal except for one.
Try to find it!

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance. Done
'''

list_sample = [0, 0, 0, 0.55, 0, 0, 0, 0, 0]


def find_uniq(list_sample):

    list_sample.sort()

    if list_sample[1] == list_sample[0]:
        unique_number = list_sample[-1]
    else:
        unique_number = list_sample[0]

    return unique_number   # n: unique integer in the array


print(find_uniq(list_sample))
