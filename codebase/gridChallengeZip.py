def gridChallengeZip(grid):
    # Write your code here

    s_grid = [sorted(_) for _ in grid]
    print(s_grid)
    print(list(zip(*s_grid)))
    arr1  = [list(i) for i in zip(*s_grid)]
    arr2 = [sorted(list(i)) for i in zip(*s_grid)]
    print(arr1)
    print(arr2)
    return 'YES' if arr1 == arr2 else 'NO'

if __name__ == '__main__':
    gr = ['abc', 'ade', 'efg',
          # 'ndh',
          # 'ekz'
          ]
    print(gridChallengeZip(gr))