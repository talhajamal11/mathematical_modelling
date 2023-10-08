"""
Given an array of integers, return the occurence of each elements
"""

import random

def count_int(numbers: list) -> dict:
    """
    return dictionary
    """
    seen = {}
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    return seen

nums = [random.randint(1, 5) for _ in range(10)]
print(nums)
print(count_int(nums))
