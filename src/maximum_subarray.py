"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""

numbers = [-2,1,-3,4,-1,2,1,-5,4]

def max_sub_array(nums: list) -> int:
    """
    Find subarrays - if new sum is larger, 
    change the largest subarray pointers
    max_sum = sum(nums[0:1])
    for left in range(0, len(nums)):
        right = left + 1
        while right <= len(nums):
            total = sum(nums[left: right])
            max_sum = max(max_sum, total)
            right += 1
    return max_sum
    """
    # kadane's algorithm with o(n)
    current_max = overall_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        overall_max = max(overall_max, current_max)
    return overall_max

print(max_sub_array(numbers))
