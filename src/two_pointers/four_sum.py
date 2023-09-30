"""
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
def two_sum(nums: list, target: int) -> any:
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        if total > target:
            right -= 1
        if total == target and nums[left] != nums[right]:
            return [nums[left], nums[right]]
    return []

def three_sum(nums: list, target: int) -> list:
    result = []
    for index, number in enumerate(nums):
        remaining = target - number
        two_sum_list = two_sum(nums[index + 1: ], remaining)
        if len(two_sum_list) != 0 and number not in two_sum_list:
            two_sum_list.append(number)
            #result.append(two_sum_list)
            return two_sum_list
    return []

def fourSum(nums: list, target: int) -> list:
    # Take a number - treat it then as a threesum problem
    # threesum: take a number - then treat it as a two sum problem
    nums.sort()
    result = []
    for index, number in enumerate(nums):
        remaining = target - number
        threesum_list = three_sum(nums[index + 1:], remaining)
        if len(threesum_list) != 0 and number not in threesum_list:
            threesum_list.append(number)
            result.append(threesum_list)
    return result

numbers = [1,0,-1,0,-2,2]
value = 0

print(fourSum(numbers, value))
