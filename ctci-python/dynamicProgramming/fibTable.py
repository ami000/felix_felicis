def fibT (n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n + 1):
        if i + 1 <= n: table[i + 1] += table[i]
        if i + 2 <= n: table[i + 2] += table[i]
    return table[n]

if __name__ == '__main__':
    print(fibT(10))