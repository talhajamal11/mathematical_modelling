"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""

def trap_water(height:list) -> int:
    """
    Return Integer
    """
    left, right = 0, len(height) - 1
    left_max, right_max, water = 0, 0, 0
    # Left Max is the height of the tower on the left and vice versa
    while left < right:
        if height[left] < height[right]:
            if height[left] < left_max:
                water += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else: # height[left] > height[right]:
            if height[right] < right_max:
                water += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_water(height))