""" 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from collections import defaultdict

def groupAnagrams(strs) -> list:
    """ 
    return list of lists
    """
    res = defaultdict(list) # mapping charCount to list of anagram strings
    for s in strs:
        count = [0] * 26 # a ... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
