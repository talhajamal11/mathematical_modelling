""" 
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
"""

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))