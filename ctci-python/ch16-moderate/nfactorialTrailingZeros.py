import math


def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact

def trailingZeros(n):
    countZeros = 0
    strN = str(factorial(n))
    for i in range(len(strN) - 1, -1, -1):
        if strN[i] == '0':
            countZeros += 1
        else:
            break
    return countZeros

def trailingZerosOptimized(n):
    if n < 0:
        return -1

    zeros = 0
    while n >= 5:
        n //= 5
        zeros += n
    return zeros



if __name__ == '__main__':
    n1 = 5
    n2 = 11
    n3 = 20
    n4 = 10000

    print(trailingZerosOptimized(n1))
    print(trailingZerosOptimized(n2))
    print(trailingZerosOptimized(n3))
    print(trailingZerosOptimized(n4))