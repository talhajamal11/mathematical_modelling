""" 
You are given three integers: i, j, and k. Sum from i to j. Sum from j to k. Return total of the sums. 
i, j, k can all be negative or positive. 
Example: i = 5, j = 9, k = 6 - Result = 56
"""

def seq_summation(i, j, k):

    def helper(num1, num2):
        return(num2 - num1 + 1) * num1 + (num2 - num1)*(num2 - num1 + 1) / 2
    
    return int(helper(i, j) + helper(k, j-1))

def solution(i, j, k):
    def helper(num):
        return (num*(num+1)) / 2
    sum1 = helper(j) - helper(i-1)
    sum2 = helper(j-1) - helper(k-1)
    return int(sum1+sum2)

print(solution(-5,5,-5))

#print(seq_summation(-5,0,-5))