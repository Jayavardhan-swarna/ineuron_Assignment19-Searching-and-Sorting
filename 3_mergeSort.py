def mergeSort(nums, start, end):
    if start >= end:
        return [nums[start]]

    mid = (start + end) // 2
    left = mergeSort(nums, start, mid)
    right = mergeSort(nums, mid + 1, end)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def sortArray(nums):
    return mergeSort(nums, 0, len(nums) - 1)


# Example 1
nums = [5, 2, 3, 1]
sorted_nums = sortArray(nums)
print(sorted_nums)
# Output: [1, 2, 3, 5]

# Example 2
nums = [5, 1, 1, 2, 0, 0]
sorted_nums = sortArray(nums)
print(sorted_nums)
# Output: [0, 0, 1, 1, 2, 5]
