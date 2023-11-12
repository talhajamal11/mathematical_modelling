""" 
Maximum sub-array sum with at most k length - the subarray must be contiguous
"""
import random
import time

array = [4, 3, -2, 9, -4, 2, 7]
k = 6

def solution(arr, k):

    def helper( arr, length, k ):
        total_sum = 0
        max_sum = 0
        for x in range( 0, length ):
            total_sum = total_sum + arr[x]
            if x >= k:
                total_sum = total_sum - arr[x - k]
            if x >= k - 1:
                max_sum = max( max_sum, total_sum )
        return max_sum

    answer = 0
    for x in range(1, k + 1):
        answer = max( answer, helper(arr, len(arr), x) )
    return answer


# print(solution(array, k))

# Example usage
#print(optimized_solution(array, k))

def dp_solution(arr, k):
    currSum = arr[0]
    maxSum = arr[0]
    for i in range(1, k):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)
        
    currSum = maxSum
    max_profit = 0
    for i in range(k, len(arr)):
        prev = arr[i-k]
        new = arr[i]
        currSum =  currSum - prev + new
        max_profit = max(max_profit, currSum)
    return max_profit

dp_solution(array, k)

def new_solution(arr, k):

    def kadane(arr):
        currSum = arr[0]
        maxSum = arr[0]
        for i in range(1, len(arr)):
            currSum = max(arr[i], currSum + arr[i])
            maxSum = max(maxSum, currSum)
        return maxSum

    max_profit = 0

    for i in range(len(arr) - k + 1):
        max_profit = max(max_profit, kadane(arr[i:k + i]))

    return max_profit

#print(new_solution([-5, -2, -1], 2))

def max_subarray_sum_of_length_k(arr, k):
    # Edge case: If k is larger than the array length, use standard Kadane's algorithm
    if k >= len(arr):
        return kadane(arr)

    # Initialize variables
    max_sum = sum(arr[:k])
    current_sum = max_sum

    # Slide the window
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

def kadane(arr):
    # Implementation of Kadane's algorithm
    current_sum = max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


arr = [random.randint(-9, 9) for _ in range(10000000)]
start = time.time()
result = dp_solution(arr, 10)
stop = time.time()
print(stop - start)