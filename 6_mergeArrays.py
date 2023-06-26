def mergeArrays(arr1, arr2):
    i = 0
    j = 0
    k = 0
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [0] * (n1 + n2)

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr3[k] = arr2[j]
        j += 1
        k += 1

    return arr3


# Example 1
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
result = mergeArrays(arr1, arr2)
print(result)
# Output: [1, 2, 3, 4, 4, 5, 6, 8]

# Example 2
arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
result = mergeArrays(arr1, arr2)
print(result)
# Output: [4, 5, 7, 8, 8, 9]
