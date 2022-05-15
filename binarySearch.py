import math
test_case_number = 1

def printValue(n):
    print('[', n, ']', sep='', end='')

def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printValue(expected)
        print(' Your output: ', end='')
        printValue(output)
        print()
    test_case_number += 1

def binarySearch (array, target):
    left  = 0
    right = len(array) - 1
#     find middle

    while left <= right:
        middle = math.floor((left + right) / 2)
        if array[middle] == target:
            return middle
        elif target < array[middle]: #
            right = middle - 1
        else:
            left = middle + 1
    return -1

if __name__ == "__main__":
    # Testcase 1
    array1 = [10, 34, -81, 68, 123, 9999, 907891, 109842, -309]
    sorted_array1 = sorted(array1)
    target1 = 10
    expected_1 = 2
    output_1 = binarySearch(sorted_array1, target1)
    check(expected_1, output_1)

    # Testcase 2
    target2 = 198
    expected_2 = -1
    output_2 = binarySearch(sorted_array1, target2)
    check(expected_2, output_2)

    # print(binarySearch(sorted_array1, sorted_array1[0] - 1)) # first element - 1
    # for target in sorted_array1:
    #     print(binarySearch(sorted_array1, target))