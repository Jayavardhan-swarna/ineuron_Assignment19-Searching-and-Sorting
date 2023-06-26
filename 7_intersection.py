def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = []

    for num in nums2:
        if num in set1 and num not in intersection:
            intersection.append(num)

    return intersection


# Example 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result)
# Output: [2]

# Example 2
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersection(nums1, nums2)
print(result)
# Output: [9, 4]
