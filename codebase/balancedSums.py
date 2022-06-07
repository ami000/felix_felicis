def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    leftsum = 0
    iRemovedLeftSum = 0
    res = 'NO'
    for i in range(len(arr)):
        leftsum += arr[i]
        if i == 0:
            continue
        else:
            iRemovedLeftSum = leftsum - arr[i]
            print(iRemovedLeftSum)
            rightsum = total - leftsum
            print(rightsum)
            if rightsum == iRemovedLeftSum:
                res = 'YES'
    return res


if __name__ == '__main__':
    arr1 = [2, 0, 0, 0]
    print(balancedSums(arr1))