"""


"""

def total_fruit(fruits: list) -> int:
    """
    Find longest subarray with 2 distinct numbers
    """
    left, right = 0, 0
    seen = {}
    max_length = 0
    #for right, fruit in enumerate(fruits):
    while right < len(fruits):
        fruit = fruits[right]
        if fruit not in seen and len(seen) <= 1:
            seen[fruit] = True
            max_length = max(max_length, right - left + 1)
            right += 1
        elif fruit in seen:
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            left += 1
            right = left
            seen = {}
    return max_length

values = [0,1,6,6,4,4,6]
print(total_fruit(values))
