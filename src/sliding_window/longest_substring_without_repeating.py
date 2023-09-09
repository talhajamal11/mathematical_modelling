"""
Find the length of the longest substring in a string without repeating characters
"""

phrase = "abcbbaadvbc"

def longest_without_repeating(word: str) -> any:
    """
    Return the longest substring without repeating characters 
    and the length of it
    """
    left = 0
    right = 1
    length = 0
    seen = {} # hashmap for characters
    while right < len(word):
        # Iterate from left all the way to the right
        
