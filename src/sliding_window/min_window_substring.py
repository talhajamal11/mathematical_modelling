"""
Min Window Substring
"""
def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    window, needCount = {}, {}
    for i in range(len(t)):
        needCount[t[i]] = 1 + needCount.get(t[i], 0)
    have, need = 0, len(needCount)
    left = 0
    res, res_length = [-1, -1], float("infinity")
    for right in range(len(s)):
        char = s[right]
        window[char] = 1 + window.get(char, 0)
        if char in needCount and window[char] == needCount[char]:
            have += 1
        while have == need:
            if (right - left + 1) < res_length:
                res = [left, right]
                res_length = right - left + 1
            window[s[left]] -= 1
            if s[left] in needCount and window[s[left]] < needCount[s[left]]:
                have -= 1
            left += 1
    L, R = res
    return s[L:R+1] if res_length != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
