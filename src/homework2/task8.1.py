# here is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.


arr = [0, 0, 0, 0.55, 0, 0, 0, 0, 0]


def find_uniq(arr):

    if arr[1] == arr[0]:
        a = arr[0]
    elif arr[2] == arr[0]:
        a = arr[0]
    else:
        a = arr[2]
    print(a)

    for number in arr:
        if number != a:
            n = number

    return n   # n: unique integer in the array


print(find_uniq(arr))
