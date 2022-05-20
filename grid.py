def gridChallenge(grid):
    sortedGrid = [sorted(_) for _ in grid]
    if sorted(sortedGrid) == sortedGrid:
        return 'YES'
    else:
        return 'NO'
# Write your code here

if __name__ == '__main__':
    gr = ['abc', 'ade', 'efg', 'erj', 'ndh']
    print(gridChallenge(gr))