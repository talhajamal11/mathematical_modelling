# Find the maximum sum from a subset of an array

def maxSubsetSum(arr):
    res = [arr[-1],arr[-2]]
    for i in range(len(arr)-3,-1,-1):
            tmp = max(res[:-1])
            if arr[i]+tmp > arr[i]:
                res = [tmp,res[-1]]
                res.append(res[0]+arr[i])
            else:
                res.append(arr[i])

    return max(res)

arr = [-1, -3, 4, 2]
print(maxSubsetSum(arr))