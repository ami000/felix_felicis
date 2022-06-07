def  grid_traveller(m, n, memo={}):
    key = f'{m},{n}'
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)

    return memo[key]

# Driver code
if __name__ == '__main__':
    n1, m1 = 3, 3
    n2, m2 = 3, 2
    # n3, m3 = 18, 18

    print(grid_traveller(n1, m1), grid_traveller(n2, m2), grid_traveller(n3, m3))