"""
| cwd      | cd (arg)       | output
| -------- | -------------- | ------
| /        | foo            | /foo
| /baz     | /bar           | /bar
| /foo/bar | ../../../../.. | /
| /x/y     | ../p/../q      | /x/q
| /x/y     | /p/./q         | /p/q
"""


# def changeDirectory(cwd, cd):
#     cwdArray = cwd.split('/')
#     cdArray = cd.split('/')
#
#     if cwdArray == []:
#         return f'/{cd}'
#
#     for i in cdArray:
#         if cdArray[i] == '..':
#             cwdArray.pop()
#         if cdArray[i] == '.':
#             continue
#         else:
#             cwdArray.append(cdArray[i])
#     return '/'.join(cwdArray)


"""
Given a matrix of integers print out its values along the diagonals that move in the top right to bottom left direction. Each diagonal goes down and to the left as shown in the example. There should be newlines between each diagonal.

For example, given this matrix:
[[1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12]]
The print out should be:
1
2 5
3 6 9
4 7 10
8 11 
12 
"""


def matrixDiagonal(arr):
    out = []
    for i in range(len(arr) - 1):  # i=1, len(arr)=3
        if i == 0: print(arr[0][0])
        negativeArr = arr[0][:i]  # negativeArr=[1, 2, 3, 4]
        for j in range(len(negativeArr) - 1, -1, -1):
            print(arr[i + 1][j])

if __name__ == '__main__':
    arr1 = [[1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12]]
    print(matrixDiagonal(arr1))



