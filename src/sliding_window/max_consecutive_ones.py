"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

numbers = [1,1,1,0,0,0,1,1,1,1,0]
replacements = 2

def longestOnes(nums: list, k: int) -> int:
    """
    return longest subarray with 1s
    count = {}
    left, length = 0, 0
    for right, number in enumerate(nums):
        count[number] = 1 + count.get(number, 0)
        if ((right - left + 1) - (count.get(1, 0))) > k:
            count[nums[left]] -= 1
            left += 1
        length = max(length, right - left + 1)
    return length
    """
    count = {}
    max_length, left = 0, 0
    for right, number in enumerate(nums):
        count[number] = 1 + count.get(number, 0)
        while (right - left + 1 - max(count.values())) > k:
            count[nums[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(longestOnes(numbers, replacements))
