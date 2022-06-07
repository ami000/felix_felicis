import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

def shiftHelper(index, k, typeChar='alpha'):
    res = 0
    limit = 26 if typeChar == 'alpha' else 10
    if index + k > limit:
        res = (index + k) % limit
    elif index + k == limit or index == limit:
        res = 0
    else:
        res = index + k
    return res


def rotationalCipher(input, rotation_factor):
    # Write your code here
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabets = alphabets.upper()

    list_lower = list(alphabets)
    list_upper = list(upper_alphabets)

    numbers = list('0123456789')

    s = list(input)

    for i in range(len(s)):
        # print('entered for loop')
        if s[i] in numbers:
            curr_num_index = numbers.index(s[i])
            newIndex = shiftHelper(curr_num_index, rotation_factor, 'num')
            s[i] = numbers[newIndex]
        elif s[i] in list_lower:
            curr_lower_index = list_lower.index(s[i])
            newIndex = shiftHelper(curr_lower_index, rotation_factor)
            s[i] = list_lower[newIndex]
        elif s[i] in list_upper:
            currentIndex = list_upper.index(s[i])
            newIndex = shiftHelper(currentIndex, rotation_factor)
            s[i] = list_upper[newIndex]

    return ''.join(s)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    input_3 = "Zebra-493"
    rotation_factor_3 = 3
    expected_3 = "Cheud-726"
    output_3 = rotationalCipher(input_3, rotation_factor_3)
    check(expected_3, output_3)

    # Add your own test cases here
