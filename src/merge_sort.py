def merge(arr1, arr2):
    new_arr = []

    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
            continue

        new_arr.append(arr2.pop(0))

    while arr1:
        new_arr.append(arr1.pop(0))

    while arr2:
        new_arr.append(arr2.pop(0))

    return new_arr


def divide(arr):
    if len(arr) == 1:
        return arr

    left = []
    right = []
    middle = len(arr) // 2

    for i in range(middle):
        left.append(arr[i])

    for i in range(middle, len(arr)):
        right.append(arr[i])

    return merge(divide(left), divide(right))


def sort_array_by_merge_sort(values):
    sorted_arr = divide(values)
    return sorted_arr
