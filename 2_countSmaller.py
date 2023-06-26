def countSmaller(nums):
    def mergeAndCount(left, right):
        merged = []
        count = 0
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i])
                counts[left[i][0]] += count
                i += 1
            else:
                merged.append(right[j])
                count += 1
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def mergeSort(start, end):
        if start >= end:
            return []

        mid = (start + end) // 2
        left = mergeSort(start, mid)
        right = mergeSort(mid + 1, end)

        return mergeAndCount(left, right)

    counts = [0] * len(nums)
    indexedNums = list(enumerate(nums))
    mergeSort(0, len(indexedNums) - 1)

    return counts


# Example 1
nums = [5, 2, 6, 1]
counts = countSmaller(nums)
print(counts)
# Output: [2, 1, 1, 0]

# Example 2
nums = [-1]
counts = countSmaller(nums)
print(counts)
# Output: [0]

# Example 3
nums = [-1, -1]
counts = countSmaller(nums)
print(counts)
# Output: [0, 0]
