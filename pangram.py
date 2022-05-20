#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_list = list(alphabet)
    str_list = list(s)

    for i in str_list:
        if i.lower() in alpha_list: alpha_list.remove(i.lower())
    res = 'not pangram'
    if len(alpha_list) == 0:
        res = 'pangram'
    return res
if __name__ == '__main__':
    s = 'We promptly judged antique ivory buckles for the next prize'
    result = pangrams(s)
    print(result)

    s = 'We promptly judged antique ivory buckles for the prize'
    result = pangrams(s)
    print(result)