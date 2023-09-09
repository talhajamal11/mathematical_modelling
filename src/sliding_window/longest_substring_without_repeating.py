"""
Find the length of the longest substring in a string without repeating characters
"""

phrase = "bbbb"

def longest_without_repeating(word: str) -> any:
    """
    Return the longest substring without repeating characters 
    and the length of it
    """
    left = 0
    length, max_length = 0, 0
    seen = {} # hashmap for characters
    for right, char in enumerate(word):
        # Iterate from left all the way to the right
        if char not in seen:
            # push to dictionary
            seen[char] = True
            length = len(word[left:right + 1])
            max_length = max(max_length, length)
        elif char in seen:
            # found duplicate
            left += 1
            seen = {}
    return max_length

print(longest_without_repeating(phrase))
