"""
Longest Repeating Character Replacement
"""

def characterReplacement(s: str, k: int) -> int:
    alphabets = {}
    left = 0
    max_length = 0
    for right, alpha in enumerate(s):
        # add alphabet to dictionary
        alphabets[alpha] = 1 + alphabets.get(alpha, 0)
        while (right - left + 1) - (max(alphabets.values())) > k:
            alphabets[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

sentence = "AABABBA"
k = 1
print(characterReplacement(sentence, k))
    