import numpy as np

def dynamicArray(n, queries):
    # Write your code here
    arr = np.arange(n*1).reshape(n*1)
    print(arr)
    lastAnswer = 0


if __name__ == '__main__':
    num = 2
    q = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0],  [2, 1, 1]]

    print(dynamicArray(num, q))