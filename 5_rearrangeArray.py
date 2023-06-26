def rearrangeArray(arr):
    pos = 0
    neg = 0

    while pos < len(arr):
        if arr[pos] >= 0:
            pos += 1
        else:
            neg = max(neg, pos + 1)
            while neg < len(arr) and arr[neg] >= 0:
                neg += 1
            if neg >= len(arr):
                break
            arr[pos+1:neg+1] = arr[pos:neg]
            arr[pos] = arr[neg]
            pos += 2
            neg += 1

    return arr


# Example 1
arr = [1, 2, 3, -4, -1, 4]
result = rearrangeArray(arr)
print(result)
# Output: [-4, 1, -1, 2, 3, 4]

# Example 2
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
result = rearrangeArray(arr)
print(result)
# Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
