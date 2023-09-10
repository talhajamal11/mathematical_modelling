"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums 
contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

numbers = [1, 1, 1, 1 ,2]
# Output Expected: 2, nums = [1,2,_]

def removeDuplicates(nums: list) -> int:
    """
    remove duplicates
    right pointer moves around aray
    left pointer stays to the position where number has to be inserted
    """
    left = 0
    seen = {}
    for right, number in enumerate(nums):
        if right == 0:
            seen[number] = True
            left += 1
        elif right > 0:
            if number not in seen:
                seen[number] = True
                nums[left] = number
                left += 1
            elif number in seen:
                # dont update left - this is where next unique value should be placed
                continue
    return left, nums

def remove_duplicates(nums: list) -> int:
    """
    alt solution
    """
    left = 1
    for right in range(1 , len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left

print(remove_duplicates(numbers))
