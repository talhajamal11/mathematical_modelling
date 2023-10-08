"""
Leetcode 11: Container with the most water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

def max_area(height: list) -> int:
    """
    Return Integer
    """
    # We need maximum area in an array - start with two pointers as wide as possible
    left = 0
    right = len(height) - 1
    curr_max, real_max = 0, 0
    while left < right:
        # the height will be the min height of the two pillars
        h = min(height[left], height[right])
        length = right - left
        curr_max =  h * length
        real_max = max(curr_max, real_max)
        # We will change pointers when we find a height taller than the tallest height
        if height[left] < height[right]:
            # increment left
            index = left
            while left < right and height[index] >= height[left]:
                left += 1
        else:
            # decrement right
            index = right
            while left < right and height[index] >= height[right]:
                right -= 1
    return real_max

print(max_area([1,8,6,2,5,4,8,3,7]))
