grid1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"]
]
grid2 = [
  ["L","L","W","W","W"],
  ["L","L","W","W","W"],
  ["W","W","L","W","W"],
  ["W","W","W","L","L"]
]

def  islandCount(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if explore(grid, r, c, visited):
                count += 1
    return count

def explore(grid, r, c, visited):
    rowInbounds  = 0 <= r < len(grid)
    colInbounds  = 0 <= c < len(grid)
    if not rowInbounds or not colInbounds: return False
    if grid[r][c] == 'W': return False
    pos = (r, c)

    if pos in visited: return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True

if __name__ == '__main__':
    print(islandCount(grid1))
    print(islandCount(grid2))