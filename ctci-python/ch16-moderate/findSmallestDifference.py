import math

def findSmallestDifference(a1, a2):
    a = 0
    b = 0
    diff = math.inf
    a1, a2 = sorted(a1), sorted(a2)
    while a < len(a1) and b < len(a2):
        if abs(a1[a] - a2[b]) < diff:
            diff = abs(a1[a] - a2[b])
        if a1[a] < a2[b]:
            a += 1
        else:
            b += 1
    return diff

if __name__ == '__main__':
    a4 = [1, 2, 3, 4, 5, 80]
    b1 = [ 8, 61, 89, 13, -1]
    b2 = [8, 61, 89, 13, 81]
    b3 = []
    b4 = [ 8, 61, 89, 13, -1]

    print(findSmallestDifference(a4, b1))
    print(findSmallestDifference(a4, b2))
    print(findSmallestDifference(a4, b3))
    print(findSmallestDifference(a4, b3))