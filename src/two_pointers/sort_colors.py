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
    # use pointers 
    # base case
    if len(nums) == 0 or len(nums) == 1:
        return
    left = 0 # put all 0s to the left position and increment left
    right = len(nums) - 1 #put all 2s to the right most position and decrement right
    index = 0
    while index <= right and left < right:
        # iterate through whole array till you reach right
        # or left and right are the same
        if nums[index] == 0:
            # Move the current index value to the left index position
            # Assign 0 to the left index
            nums[index] = nums[left]
            nums[left] = 0
            left += 1
        if nums[index] == 2:
            nums[index] = nums[right]
            nums[right] = 2
            right -= 1
        else:
            # num is a 1
            index += 1
    return


numbers = [2,0,1]
print(sort_colors(numbers))
