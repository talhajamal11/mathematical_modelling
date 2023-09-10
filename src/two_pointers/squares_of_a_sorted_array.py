"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""
nums = [-4,-1,0,3,10]

def sortedSquares(nums: list) -> list:
    """
    return list of square array
    """
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        if nums[left] ** 2 < nums[right] ** 2:
            result.append(nums[right] ** 2)
            right -= 1
        else:
            result.append(nums[left] ** 2)
            left += 1
    return result[::-1]
print(sortedSquares(nums))
