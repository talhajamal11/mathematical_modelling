"""
Return all subarrays with product less than K
"""

def numSubarrayProductLessThanK(nums: list, k: int) -> int:
    """
    Return int
    """
    """
    Brute Force Method
    result = []
    for index, number in enumerate(nums):
        end = index + 1
        while end <= len(nums):
            sub_array = nums[index: end]
            product = 1
            for num in sub_array:
                product = product * num
            if product < k:
                result.append(sub_array)
                end += 1
                continue
            else:
                end += 1
    return len(result)
    """
    # Efficient algorithm using two pointers
    # base case
    if k <= 1:
        return 0
    
    # Sliding Window technique
    left, right = 0, 0
    result = 0
    product = 1
    while right < len(nums):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        result += right - left + 1
        right += 1
    return result

numbers = [1,2,3]
K = 0

print(numSubarrayProductLessThanK(numbers, K))
