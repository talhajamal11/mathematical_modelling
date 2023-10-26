# Find the maximum sum from a subset of an array

def maxSubsetSum(arr):
    n = len(arr)
    if n == 1:
        return max(0, arr[0])
    max_sum = [0] * n
    max_sum[0] = max(0, arr[0])
    max_sum[1] = max(max_sum[0], arr[1])
    for i in range(2, n):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + arr[i])
    return max(max_sum[-1], 0)

arr = [-2, 1, 3, -4, 5]
print(maxSubsetSum(arr))