"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you 
may not use the same element twice.
You can return the answer in any order.
"""

nums = [2,7,11,15]
target = 9

def twoSum(nums: list, target: int) -> list:
    """
    return list
    """
    seen = {}
    for index, number in enumerate(nums):
        diff = target - number
        if diff in seen:
            return [seen[diff], index]
        else:
            seen[number] = index

print(twoSum(nums, target))
