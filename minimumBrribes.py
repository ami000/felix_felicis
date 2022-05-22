def minimumBribes(q):
    # Write your code here
    n = len(q)
    sortedQ = sorted(q)
    bribes = 0

    for i in range(n - 1, 0, -1):
        if q[i] != n:
            if q[i - 1] == n:
                bribes += 1
                q.pop(i - 1)
            elif q[i - 2] == n:
                bribes += 2
                q.pop(i - 2)
            else:
                return 'Too chaotic'
        else:
            q.pop(i)
        n -= 1
    return bribes

if __name__ == '__main__':
    s1 = [2, 1, 5, 3, 4]
    s4 = [2, 5, 1, 3, 4]
    s2 = [5, 1, 2, 3, 7, 8, 6, 4]
    s3 = [1, 2, 5, 3, 7, 8, 6, 4]

    print(minimumBribes(s3))