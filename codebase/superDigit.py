def superDigit(n, k):
    # Write your code here
    p = int(''.join([n] * k))
    return p

if __name__ == '__main__':
    n1 = '9875'
    k1 = 4

    print(superDigit(n1, k1))
