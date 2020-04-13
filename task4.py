def merge(arr, left_index, middle, right_index):
    n1 = middle - left_index + 1
    # n1 for amount of element in left side

    n2 = right_index - middle
    # n2 for amount of element in right side

    left_side = [0] * n1
    # left = [0, 0, 0, 0, 0, 0]

    right_side = [0] * n2
    # right = [0, 0, 0, 0, 0, 0]

    for i in range(0, n1):
        left_side[i] = arr[left_index + i]
    # copy from arr list to left side list

    for j in range(0, n2):
        right_side[j] = arr[middle + 1 + j]
    # copy from arr list to right side list

    i, j, k = 0, 0, left_index
    # i start index for left side list
    # j start index for right side list
    # k start index for middle of the list

    while i < n1 and j < n2:
        if left_side[i] <= right_side[j]:
            arr[k] = left_side[i]
            i += 1
        else:
            arr[k] = right_side[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_side[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_side[j]
        j += 1
        k += 1


# function for split the list to 2
def mergeSort(arr, left_index, right_index):
    if left_index < right_index:
        middle = int((left_index + (right_index - 1)) / 2)
        mergeSort(arr, left_index, middle)
        mergeSort(arr, middle + 1, right_index)
        merge(arr, left_index, middle, right_index)


input_list = [38, 27, 1, 43, 3, 9, 82, 10]
n = len(input_list)
print("Before Element")
for x in input_list:
    print("%d" % x, end=",")

mergeSort(input_list, 0, n - 1)
print("\n\nAfter Element")
for x in input_list:
    print("%d" % x, end=",")
