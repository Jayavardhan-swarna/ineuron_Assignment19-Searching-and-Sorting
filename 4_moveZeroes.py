def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums

# Example 1
nums = [1, 2, 0, 4, 3, 0, 5, 0]
result = moveZeroes(nums)
print(result)
# Output: [1, 2, 4, 3, 5, 0, 0, 0]

# Example 2
nums = [1, 2, 0, 0, 0, 3, 6]
result = moveZeroes(nums)
print(result)
# Output: [1, 2, 3, 6, 0, 0, 0]
