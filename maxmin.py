def maxMin(k, arr):
    # Write your code here
    sortedArray = sorted(arr)
    ksubArr = sortedArray[0: k]
    print(ksubArr)
    minUnfairness = max(ksubArr) - min(ksubArr)
    print(minUnfairness)
    return minUnfairness


if __name__ == '__main__':
    k1 = 3
    arr1  = [10, 100, 300, 200, 1000, 20, 30]
    k2  = 2
    arr2 = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629]
    print(maxMin(k1, arr1))
    print(maxMin(k2, arr2))