"""
Given an integer array nums, return all the triplets [nums[i], 
nums[j], nums[k]] such that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

def three_sum(nums: list) -> list:
    """
    return list
    """
    result = []
    nums.sort()
    for index, number in enumerate(nums):
        # Current Index will be the first number
        # we dont want number to repeat
        if index > 0 and number == nums[index - 1]:
            # go to next number
            continue
        # find two sum using left and right pointers
        left = index + 1
        right = len(nums) - 1
        while left < right:
            threeSum = number + nums[left] + nums[right]
            if threeSum < 0:
                left += 1
            elif threeSum > 0:
                right -= 1
            else:
                result.append([number, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))