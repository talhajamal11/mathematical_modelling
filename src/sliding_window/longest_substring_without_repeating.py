"""
Find the length of the longest substring in a string without repeating characters
"""
def longest_without_repeating(s: str) -> any:
    """
    Return the longest substring without repeating characters 
    and the length of it
    """
    seen, left, max_length= {}, 0, 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left: # Repeat Character
            left = seen[char] + 1
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length

phrase = "pwwkew"
print(longest_without_repeating(phrase))
