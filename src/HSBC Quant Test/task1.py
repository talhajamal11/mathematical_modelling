""" 
smallest string
print(ord('a'))
print(ord('b'))

if 'a' > 'b':
    print('False')
else:
    print("True")
"""

string = "eeeeea"

"""
def smallest_string(text):
    res = ""
    length = len(text)
    for i in range(length - 1):
        if (text[i] > text[i + 1]):
"""

def solution(s):
    min_string = s[1:]
    for i in range(1, len(s)):
        temp = s[:i] + s[i+1:]
        if temp < min_string:
            min_string = temp
    return min_string

def optimal_solution(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return s[:i] + s[i + 1:]
    return s[:-1]

print(optimal_solution(string))
