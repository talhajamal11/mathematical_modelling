""" 
A string S containing only the letters "A", "B" and "C" is given. The string can be transformed by removing one 
occurrence of "AA", "BB" or "CC".

Transformation of the string is the process of removing letters from it, based on the rules described above. 
As long as at least one rule can be applied, the process should be repeated. If more than one rule can be used, 
any one of them could be chosen.

Write a function:

def solution(S)
that, given a string S consisting of N characters, returns any string that can result from a sequence of transformations 
as described above.

For example, given string S = "ACCAABBC" the function may return "AC", because one of the possible
sequences of transformations is as follows:



Also, given string S = "ABCBBCBA" the function may return "", because one possible sequence of 
transformations is:

Finally, for string S = "BABABA" the function must return "BABABA", because no rules can be applied to string S.
"""