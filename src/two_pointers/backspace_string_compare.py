"""
Given two strings s and t, return true if they are equal when both are typed into
empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""

def backspace_compare(s: str, t: str) -> bool:
    """
    Return Boolean Values
    """
    s_pointer = len(s) - 1
    t_pointer = len(t) - 1

    s_skips = 0
    t_skips = 0

    while s_pointer >= 0 or t_pointer >= 0:

        while s_pointer >= 0:
            if s[s_pointer] == '#':
                s_skips += 1
                s_pointer -= 1
            elif s_skips > 0:
                s_pointer -= 1
                s_skips -= 1
            else:
                break

        while t_pointer >= 0:
            if t[t_pointer] == '#':
                t_skips += 1
                t_pointer -= 1
            elif t_skips > 0:
                t_pointer -= 1
                t_skips -= 1
            else:
                break
        
        if s_skips >= 0 and t_skips >= 0 and s[s_pointer] != t[t_pointer]:
            return False

        if (s_pointer >= 0) != (t_pointer >= 0):
            return False
         
        s_pointer -= 1
        t_pointer -= 1

    return True


STRING_1 = "b#c"
STRING_2 = "ad#c"
print(backspace_compare(STRING_1, STRING_2))
