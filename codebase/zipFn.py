def zipFn(inp):
    for i in zip(inp):
        print(i)
    return [i for i in zip(inp)]
if __name__ == '__main__':
    n = [1, 2, 3, 4, 5]
    x = [[0, 1], [0]]
    z =  [[1,2,3,4],[1,2,3],[1,2,3,4,5]]
    print(zipFn(z))