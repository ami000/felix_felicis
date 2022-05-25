def iceCreamParlour(m, arr):
    # Write your code here
    valueIndexDict = {}
    for i in range(len(arr)):
        if arr[i] in valueIndexDict:
            return [valueIndexDict[arr[i]] + 1, i + 1]
        else:
            diff = m - arr[i]
            valueIndexDict[diff] = i



if __name__ == '__main__':
    m1 = 4
    arr1  = [1, 4, 5, 3, 2]
    arr2 = [2, 2, 4, 3]

    # arr1  = [10, 100, 300, 200, 1000, 20, 30]
    m2  = 4
    # arr2 = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629]
    print(iceCreamParlour(m1, arr1))
    print(iceCreamParlour(m2, arr2))