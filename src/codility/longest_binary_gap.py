"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is 
surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 
and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. 
The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 
100000 and has no binary gaps.

Write a function:

def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
"""

def binary_rep(number):
    return bin(number)[2:]

def binary_gap(number):
    binary_num = binary_rep(number)
    length, max_length = 0, 0
    left = 0
    for right in range(len(binary_num)):
        char = int(binary_num[right])
        if char == 1:
            length = right - left - 1
            max_length = max(max_length, length)
            left = right
    return max_length

print(binary_gap(32))