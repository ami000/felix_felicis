import math


def pageCount(n, p):
    res = 0
    neven = n % 2 == 0
    if p == 1 or p == n:
        pass
    else:
        if p == n - 1:
            if neven:
                res = 1
            else:
                pass
        else:
            res = min(math.ceil(abs((1 - p)/2)), math.ceil(abs((n - p)/2)))
    return res

if __name__ == '__main__':
    total, page = 18183, 18042
    print(pageCount(total, page))