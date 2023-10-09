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
    while left < right:
        if height[left] < height[right]: # can contain water
            if height[left] < left_max:
                water += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else: # height[left] > height[right]
            if height[right] < right_max: # can contain water
                water += right_max - height[right]
            else:
                right_max = height[right]
            right -=1
    return water


height = [4,2,0,3,2,5]
print(trap_water(height))