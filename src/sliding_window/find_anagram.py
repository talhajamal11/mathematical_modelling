"""
Find Anagram
"""
def findAnagrams(s: str, p: str):
    s_count, p_count, left = {}, {}, 0
    if len(p) > len(s):
        return result
    for i in range(len(p)):
        p_count[p[i]] = 1 + p_count.get(p[i], 0)
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
    result = [0] if s_count == p_count else []
    for right in range(len(p), len(s)):
        s_count[s[right]] = 1 + s_count.get(s[right], 0)
        s_count[s[left]] -= 1
        if not s_count[s[left]]:
            s_count.pop(s[left])
        left += 1
        if p_count == s_count:
            result.append(left)
    return result

s = "baa"
p = "aa"
print(findAnagrams(s, p))
