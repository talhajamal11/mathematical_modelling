""" 
Write a function solution that given a string S consisting of N characters, returns the alphabetically smallest string
that can be obtained by removing exactly one letter from S.

1. S = "acb". You can obtain "ac", "ab", "cb". Your function should return "ab" since it is the smallest. 
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

#print(optimal_solution(string))

def new_solution(s):
    # acb -> ab
    res = ""
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return s[:i] + s[i+1:]
    return s[:-1]

print(new_solution("hotty"))
