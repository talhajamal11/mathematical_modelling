""" 
You have a list of strings, and get a letter K. You can pick at most K letters from a-z to form the longest
subset of your list of strings as possible, with your chosen strings only containing the letters you’ve chosen. 
What is the size of the subset you can make?
"""

def lengthOfLongestSubstringKDistinct(s, k):
    # Hashmap to store the character and its occurrence in sliding window
    seen = {}
    # Left Pointer and Maximum variable
    L, maximum = 0, 0
    # Iterate through entire string
    for R, C in enumerate(s):
        seen[C] = 1 + seen.get(C, 0)    # Count of each character
        while len(seen) > k:            # Hashmap must not have more than k characters
            seen[s[L]] -= 1             # Decrement count of character at Left Pointer
            if seen[s[L]] == 0:         # IF character count goes to 0, remove it from hashmap
                del seen[s[L]]
            L += 1                      # Increment chracter count
        maximum = max(maximum, R-L+1)   # Result will be the maximum length of the sliding window
    return maximum

strings = ['apple', 'banana', 'orange', 'kiwi', 'plum']
K = 2
maximum = 0
for string in strings:
    maximum = max(maximum, (lengthOfLongestSubstringKDistinct(string, K)))

print(maximum)

