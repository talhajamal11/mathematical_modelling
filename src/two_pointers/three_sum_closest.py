"""
Find the three_sum closest to target
"""

def three_sum_closest(nums: list, target: int) -> int:
    """
    Return Int
    """
    nums.sort()
    min_distance = float('inf')
    for index, number in enumerate(nums):
        left = index + 1
        right = len(nums) - 1
        while left < right:
            three_sum = number + nums[left] + nums[right]
            distance = abs(target - three_sum)
            if distance < min_distance:
                min_distance = distance
                result = three_sum
            if three_sum == target:
                return target
            if three_sum < target:
                left += 1
            else:
                right -= 1
    return result

numbers = [0,0,0]
TARGET = 1

print(three_sum_closest(numbers, TARGET))
