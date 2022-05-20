def findMedian(arr):
    # Write your code here
    total = len(arr)
    print(total)
    medianIndex = int(((total + 1) / 2) - 1)
    print(medianIndex)
    sortedArray = sorted(arr)
    return sortedArray[medianIndex]

if __name__ == '__main__':
    q = [1, 3, 5, 2, 4]

    print(findMedian(q))