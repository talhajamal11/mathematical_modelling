""" 
You have a list of strings, and get a letter K. You can pick at most K letters from a-z to form the longest
subset of your list of strings as possible, with your chosen strings only containing the letters you’ve chosen. 
What is the size of the subset you can make?

def solution(S, K):
    max_count = 0
    for string in S:
        seen = {}
        count = 0
        for char in string:
            seen[char]= 1 + seen.get(char, 0)
        if len(seen) > K:
            continue

        for other in S:
            bool_flag = True
            if other == string:
                count += 1
                continue
            characters = set(other)
            for character in characters:
                if character not in seen:
                    bool_flag = False
                    break
            if bool_flag:
                count += 1
        max_count = max(max_count, count)
    return max_count
"""

""" 
Questions says if you pick K letters from the alphabets, what are the maximum number of strings in array S 
that can be made with K letters
"""

S1 = ["abc", "abb", "cb", "a", "bbb"]
K1 = 2

S2 = ["adf", "jibh", "jcgj", "eijj", "adf"]
K2 = 3

S3 = ["abcd", "efgh"]
K3 = 3

S4 = ["bc", "edf", "fde", "dge", "abcd"]
K4 = 4

from collections import defaultdict

def solution(S, K):
    letter_count = {}

    for s in S:
        unique_letters = {}
        for c in s:
            unique_letters[c] = 1 + unique_letters.get(c, 0)
        for letter, count in unique_letters.items():
            letter_count[letter] = max(letter_count.get(letter, 0), count)
    
    letter_counts = list(letter_count.values())
    letter_counts.sort(reverse=True)
    
    result = 0
    for count in letter_counts:
        if K >= count:
            result += count
            K -= count
        else:
            result += K
            break
    
    return result



print(solution(S1, K1))
print(solution(S2, K2))
print(solution(S3, K3))
print(solution(S4, K4))
