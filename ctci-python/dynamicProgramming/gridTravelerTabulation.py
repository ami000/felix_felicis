def  grid_travellerT(m, n):
    table = [[0 for col in range(n+1)] for row in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j + 1 <= n : table[i][j + 1] += current
            if i + 1 <= m : table[i + 1][j] += current
    print(table)
    return table[m][n]

# Driver code
if __name__ == '__main__':
    print(grid_travellerT(3, 2))
    print(grid_travellerT(3, 3))
