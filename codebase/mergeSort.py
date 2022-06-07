def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k +=  1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_two_lists_with_keys(a, b, arr, key, descending = False):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    if descending:
        while len(a) > 0 and len(b) >  0:
            if a[i][key] >= b[j][key]:
                arr[k] = a.pop(0)
                i += 1
            else:
                arr[k] = b[j]
                j += 1
    else:
        while i < len_a and j < len_b:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k +=  1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge_two_sorted_lists(left, right, arr)

if __name__ == '__main__':
    a = [5, 8, 12, 56, 89, 100]
    b = [7, 9, 45, 51]
    arr1 = [10, 3, 15, 7, 8, 23, 98, 29]

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [0],
        [9, 8, 6, 1],
        [1, 2, 3, 4 ,5],
        ['10',' 3', '15',' 7','8', '23', '98', '29']
    ]

    for array in test_cases:
        mergeSort(array)
        print(array)

    # print(merge_two_sorted_lists(a, b))
    # print(mergeSort(arr1))

    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    # mergeSort(elements, True, 'time_hours')
    # print(elements)