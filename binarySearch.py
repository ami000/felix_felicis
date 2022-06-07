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

def binarySearch (array, target, left):
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

def binarySearchRecursive(array,  target, left_idx, right_idx):
    if right_idx < left_idx:
        return -1
    middle = (left_idx + right_idx) // 2
    if middle >= len(array) or middle < 0:
        return -1
    if array[middle] ==  target:
        return middle
    elif target < array[middle]:  #
        right_idx = middle - 1
    else:
        left_idx = middle + 1
    return binarySearchRecursive(array, target, left_idx, right_idx)

def findAllOccurrences (array, target):
    return [i for i, x in enumerate(array) if x == target]

if __name__ == "__main__":
    # Testcase 1
    array1 = [1, 4, 6, 9, 10, 5, 7]
    sorted_array1 = sorted(array1)
    target1 = 5
    expected_1 = 2
    output_3 = binarySearch(sorted_array1, target1, 0)
    check(2, output_3)
    output_1 = binarySearchRecursive(sorted_array1, target1, 0, len(array1))
    check(expected_1, output_1)

    # Testcase 2
    target2 = 198
    expected_2 = -1
    output_2 = binarySearch(sorted_array1, target2)
    check(expected_2, output_2)
    print(findAllOccurrences([1,2,3,1,2,4,5,6,3,2,1], 1))
    # print(binarySearch(sorted_array1, sorted_array1[0] - 1)) # first element - 1
    # for target in sorted_array1:
    #     print(binarySearch(sorted_array1, target))