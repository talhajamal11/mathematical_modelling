""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1

    for i in range(len(t)):
        if t[i] not in count:
            return False
        else:
            count[t[i]] -= 1
            if not count[t[i]]:
                count.pop(t[i])
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))