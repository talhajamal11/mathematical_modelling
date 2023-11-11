""" 
Write a function that, given an array A consisting of N integers, returns the maximum sum of
two numbers whose digits add up to an equal sum. If there are no two numbers whose digits
have an equal sum, the function should return -1.

Example:
A = [51, 71, 17, 42] the function should return 93 - (51, 42) and (17, 71)
A = [42, 33, 60]  the function should return 102 - (42, 60)
"""

def solution(A):
    # Implement your solution here
    def sum_of_digits(num): # Function to find the sum of digits of any number
        total = 0
        while num:
            total += (num % 10)
            num = num // 10
        return total
    
    result, hashmap = -1, {} # Initialize result to -1 and hashmap to store sums
    
    for i in range(len(A)):
        number = A[i]
        curr_sum = sum_of_digits(number)
        if curr_sum not in hashmap:
            hashmap[curr_sum] = number
        else:
            result = max(result, number + hashmap[curr_sum])
            hashmap[curr_sum] = max(hashmap[curr_sum], number)
            
    return result

#print(solution([22, 1003, 1021, 4000]))

def new_solution(arr):
    """ 
    return the max sum
    """
    def sum_digits(num):
        total = 0
        while num:
            total += num % 10
            num = num // 10
        return total

    res = {}
    max_sum = -1
    for num in arr:
        curr_sum = sum_digits(num)
        if curr_sum not in res:
            res[curr_sum] = num
        else:
            max_sum = max(max_sum, num + res[curr_sum])
            res[curr_sum] = max(res[curr_sum], num)
    return max_sum

print(new_solution([15, 33, 60, 51]))