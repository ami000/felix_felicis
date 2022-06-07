def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor

def get_median(ls):
    # sort the list
    ls_sorted = ls.sort()
    # find the median
    if len(ls) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(ls)+1)/2 - 1)
        return ls[m]
    else:
        m1 = int(len(ls)/2 - 1)
        m2 = int(len(ls)/2)
        return (ls[m1]+ls[m2])/2

def insertion_sort_running_medians(arr):
    medians = []
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor
        currentList = arr[:anchor]
        medians.append(get_median(currentList))
    return medians


if __name__ == '__main__':
    elements = [11, 9, 29, 7,  2, 15, 28]
    print(insertion_sort(elements))
    # print(insertion_sort_running_medians(elements))
    # print(elements)