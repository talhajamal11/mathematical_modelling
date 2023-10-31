"""
An array A consisting of N integers is given. An inversion is a pair of indexes (P, Q) such that P < Q and A[Q] < A[P].
Write a function:
def solution(A)
that computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.
For example, in the following array:

 A[0] = -1 A[1] = 6 A[2] = 3
 A[3] =  4 A[4] = 7 A[5] = 4
there are four inversions:

   (1,2)  (1,3)  (1,5)  (4,5)
so the function should return 4.

array = [-1,,6, 3, 4, 7, 4]
"""

# Inversion count indicates how far away the array is from being sorted
# Enhanced Merge Sort

