"""
Three Sum
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums: list) -> list:
    """
    return list
    """
    result = []
    nums.sort()
    for index, number in enumerate(nums):
        # Choose First Number
        # Make sure in second iterations there are no duplicates
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        left = index + 1
        right = len(nums) - 1
        while left < right:
            total = number + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # We have found the combo equals 0
                result.append([number, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))
