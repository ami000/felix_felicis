import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def helper(index, k):
    res = 0
    if index + k > 26:
        res = (index + k) % 26
    elif index + k == 26:
        res = 0
    else:
        res = index + k
    return res


def caesarCipher(s, k):
    # Write your code here
    lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperAlphabet = lowerAlphabet.upper()

    lowerAlphabetArray = list(lowerAlphabet)
    upperAlphabetArray = list(upperAlphabet)

    stringArray = list(s)
    print(stringArray)
    outputArray = []
    for i in range(len(stringArray)):
        print(i)
        if stringArray[i] in lowerAlphabetArray:
            index = lowerAlphabetArray.index(stringArray[i])
            finalIndex = helper(index, k)
            print(finalIndex)
            outputArray.append(lowerAlphabetArray[finalIndex])
        elif stringArray[i] in upperAlphabetArray:
            index = upperAlphabetArray.index(stringArray[i])
            finalIndex = helper(index, k)
            print(finalIndex)
            outputArray.append(upperAlphabetArray[finalIndex])
            print(outputArray)
        else:
            outputArray.append(stringArray[i])
            print(outputArray)
    return ''.join(outputArray)

if __name__ == '__main__':
    str1 = 'Hello_World!'
    k = 4
    result = caesarCipher(str1, k)
    print(result)

    str2 = 'We promptly judged antique ivory buckles for the prize'
    k = 94
    result = caesarCipher(str2, k)
    print(result)