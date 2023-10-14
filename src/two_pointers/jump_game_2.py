"""
Jump Game Two
"""
def jump(nums: list) -> int:
    if len(nums) == 1:
        return 0
    maxReach, steps, jumps = nums[0], nums[0], 0
    for index in range(1, len(nums) - 1):
        maxReach = max(nums[index] + index, maxReach)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - index
    return jumps + 1

nums = [2,3,1,1,4]
print(jump(nums))
