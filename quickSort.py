def partition(arr, start, end):
    pivot, pointer = arr[end], start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1
    arr[pointer], arr[end] =  arr[end], arr[pointer]

    return pointer


def quicksort(arr, start, end):
    if len(arr) == 0:
        return arr
    if start < end:
        pi = partition(arr, start, end)
        quicksort(arr, start, pi - 1)
        quicksort(arr, pi + 1, end)
    return arr

if __name__ == '__main__':
    arr1  = [1, 4, 5, 3, 2]
    quicksort(arr1, 0, len(arr1) - 1)
    print(arr1)