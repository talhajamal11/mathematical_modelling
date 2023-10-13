"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
def checkInclusion(s1: str, s2: str) -> bool:
    """
    Return Boolean Values
    """
    # Sliding window the size of len(s1)
    s1_count, s2_count = {}, {}
    count, left = 0, 0
    for i in range(len(s1)):
        s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
        s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)
    for right in range(len(s1), len(s2)):
        if s1_count == s2_count:
            return True
        #elif len(s1_count.keys()) == len(s2_count.keys()) :
            # Dictionary size equal yet still not equal
        else:
            s2_count[s2[left]] -= 1
            if not s2_count[s2[left]]:
                s2_count.pop(s2[left])
            left += 1
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)

    return s1_count == s2_count

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
