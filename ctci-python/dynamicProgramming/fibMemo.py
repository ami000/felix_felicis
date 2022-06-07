def fibM(n, memo = {0:0, 1:1}):
    if n in memo: return memo[n]
    if n < 0: return None

    memo[n] = fibM(n - 1) + fibM(n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fibM(6))