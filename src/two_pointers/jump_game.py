"""
Jump Game
"""
def canJump(nums: list) -> bool:
    left= 0
    maxReach = 0
    while left < len(nums) and left <= maxReach:
        maxReach = max(left + nums[left], maxReach)
        left += 1
    if left == len(nums):
        return True
    else:
        return False
    
nums = [2,3,1,1,4]
print(canJump(nums))
