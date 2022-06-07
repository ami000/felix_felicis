def findZigZagArray(arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    mid = int((n + 1) / 2) - 1
    start = mid
    end = n
    arr[start:end] = arr[start:end][::-1]
    return arr

if __name__ == '__main__':
    q = [1, 2, 3, 4, 17, 11, 5, 89, 64, 123, -3]

    print(findZigZagArray(q))