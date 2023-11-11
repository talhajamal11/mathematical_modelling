def containsNearbyDuplicate(nums, k) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices
    i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    """
    seen = {}
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i
        else: 
            if abs(i - seen[nums[i]]) <= k:
                return True
            seen[nums[i]] = i
    return False

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))