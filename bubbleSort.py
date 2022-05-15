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

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] =  array[index2]
    array[index2] = temp

def bubbleSort(array):
    is_sorted = False
    final_index = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for index in range(final_index):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)
                is_sorted = False
        final_index -= 1
if __name__ == "__main__":
    # Testcase 1
    array1 = [10, 34, -81, 68, 123, 9999, 907891, 109842, -309]
    expected_1 = sorted(array1)
    array2 = [10, 34, -81, 68, 123, 9999, 907891, 109842, -309]
    bubbleSort(array2)
    check(expected_1, array2)