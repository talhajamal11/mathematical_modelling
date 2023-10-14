"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 
1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.
"""

def two_sum_two(nums: list, target: int) -> list:
    """
    return list with 1 add to indexes
    """
    result = []
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            result = [left, right]
            return [1 + x for x in result]

numbers = [2,7,11,15]
target = 9
print(two_sum_two(numbers, target))
