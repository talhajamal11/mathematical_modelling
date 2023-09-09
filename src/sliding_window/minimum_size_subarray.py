"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""
TARGET = 7
nums = [2,3,1,2,4,3]
def min_sub_array_len(target: int, nums: list) -> int:
    """
    return the length of the subarray 
    """
    left = 0
    total = 0
    min_length = len(nums) + 1
    for right, number in enumerate(nums):
        # move right and keep adding to total
        total += number
        while total >= target:
            length = right - left + 1
            min_length = min(min_length, length)
            total -= nums[left]
            left += 1
    return min_length if min_length < len(nums) + 1 else 0


print(min_sub_array_len(TARGET, nums))
