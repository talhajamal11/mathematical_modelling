"""
Given an integer array nums, find the subarray
with the largest sum, and return its sum.
"""

def max_sub_array(numbers):
    """
    return max sum
    """
    left, total, max_total = 0, 0, sum(nums)
    for right, number in enumerate(nums):
        total += nums[right]
        max_total = max(max_total, total)
        if total == max_total:
            end = right
        if total < 0:
            left = right + 1
            total = 0
    return max_total, numbers[left: end + 1]


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))
