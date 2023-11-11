""" 
You are given three integers: i, j, and k. Sum from i to j. Sum from j to k. Return total of the sums. 
i, j, k can all be negative or positive. 
"""

def seq_summation(i, j, k):

    def sum_1_to_n(n):
        return (n*(n+1))/2

    print(sum_1_to_n())