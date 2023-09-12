"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

def sort_colors(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # base case
    if len(nums) == 0 or len(nums) == 1:
        return
    start = 0 # Place all 0s to start
    end = len(nums) - 1 # Place all 2s to end
    index = 0
    while index <= end and start < end:
        if nums[index] == 0:
            nums[index] = nums[start]
            nums[start] = 0
            start += 1
        if nums[index] == 2:
            nums[index] = nums[end]
            nums[end] = 2
            end -= 1
        else:
            index += 1
    return

numbers = [2,0,1]
print(sort_colors(numbers))
