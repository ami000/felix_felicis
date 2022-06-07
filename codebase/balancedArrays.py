import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def return_missing_balanced_numbers(input):
    # Write your code here
    frequency = {}
    maxFrequency = 0
    for item in input:
        # checking the element in dictionary
        if item in frequency:
            # incrementing the count
            frequency[item] += 1
            if frequency[item] > maxFrequency:
                maxFrequency = frequency[item]
        else:
            # initializing the count
            frequency[item] = 1
    output = {}
    for key in frequency:
        if frequency[key] < maxFrequency:
            output[key] = maxFrequency - frequency[key]
    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1


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
        print(expected)
        print(' Your output: ', end='')
        print(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # Testcase 1
    input_1 = ['a', 'b', 'abc', 'c', 'a']
    output_1 = return_missing_balanced_numbers(input_1)
    expected_1 = {'b': 1, 'abc': 1, 'c': 1}
    check(expected_1, output_1)

    # Testcase 2
    input_2 = [1, 3, 4, 2, 1, 4, 1]
    output_2 = return_missing_balanced_numbers(input_2)
    expected_2 = {2: 2, 3: 2, 4: 1}
    check(expected_2, output_2)

    # Testcase 3
    input_3 = [4, 5, 11, 5, 6, 11]
    output_3 = return_missing_balanced_numbers(input_3)
    expected_3 = {4: 1, 6: 1}
    check(expected_3, output_3)

    # Add your own test cases here
