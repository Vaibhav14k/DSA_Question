def merge(arr, s, e):
    mid = (s + e) // 2
    l1 = mid - s + 1
    l2 = e - mid
    print("l1-->", l1, "l2-->", l2)
    left = [0] * l1
    right = [0] * l2
    k = s
    for i in range(l1):
        left[i] = arr[k]
        k += 1
    k = mid + 1
    for i in range(l2):
        right[i] = arr[k]
        k += 1
    index1 = 0
    index2 = 0
    k = s

    while index1 < l1 and index2 < l2:
        if left[index1] <= right[index2]:
            arr[k] = left[index1]
            index1 += 1
        else:
            arr[k] = right[index2]
            index2 += 1
        k += 1
    while index1 < l1:
        arr[k] = left[index1]
        index1 += 1
        k += 1
    while index2 < l2:
        arr[k] = right[index2]
        index2 += 1
        k += 1

def mergeSort(arr, s, e):
    if s >= e:
        return
    mid = (s + e) // 2
    mergeSort(arr, s, mid)
    mergeSort(arr, mid + 1, e)
    merge(arr, s, e)

arr = [24, 5, 12, 90, 32, 8]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
