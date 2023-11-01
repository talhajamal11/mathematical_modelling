""" 
This is a maximum-length sequence of array elements that goes from left to right, 
and each element in the sequence is larger than the previous element
"""

arr = [6,2,5,1,7,4,8,3]

def longest_subsequence(array):
    length = [0] * (len(array))
    for i in range(len(array)):
        length[i] = 1
        for j in range(i):
            if array[j] < array[i]:
                length[i] = max(length[i], length[j] + 1)
    return max(length)

print(longest_subsequence(arr))
