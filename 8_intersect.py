def intersect(nums1, nums2):
    count_dict = {}
    intersection = []

    for num in nums1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in nums2:
        if num in count_dict and count_dict[num] > 0:
            intersection.append(num)
            count_dict[num] -= 1

    return intersection


# Example 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)
# Output: [2, 2]

# Example 2
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersect(nums1, nums2)
print(result)
# Output: [4, 9]
