array = [-11,-1,3,4,-10]

def maximum_subset(arr):
    total, max_sum = 0, 0
    for i in range(len(arr)):
        total = max(arr[i], arr[i] + total)
        max_sum = max(max_sum, total)
    return max_sum

print(maximum_subset(array))