"""
Given a string sequence and each of strings is integer. 
First you need to change strings to integer and then in this sequence 
you need to find largest difference in those integers.
"""

import random

def largest_diff(numbers: list):
    """
    return largest diff
    """
    left, right = 0, len(numbers) - 1
    curr_diff, max_diff = -float('inf'), -float('inf')

    while left < right:
        if numbers[left] > numbers[right]:
            curr_diff = numbers[left] - numbers[right]
            max_diff = max(max_diff, curr_diff)
        else:
            curr_diff = numbers[right] - numbers[left]
            max_diff = max(max_diff, curr_diff)

        if numbers[left] < numbers[right]:
            

numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers, max(numbers) - min(numbers))
