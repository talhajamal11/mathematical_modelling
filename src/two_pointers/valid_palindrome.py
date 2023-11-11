""" 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
"""

def isPalindrome(s: str) -> bool:
    res = ""
    for i in range(len(s)):
        if s[i].isalnum():
            res = res + s[i].lower()
    print(res)
    left = 0
    right = len(res) - 1
    while left <= right:
        if res[left] != res[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))