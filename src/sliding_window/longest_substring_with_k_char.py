"""

"""

import collections

def total_fruit(fruits: list) -> int:
    """
    Find longest subarray with 2 distinct numbers
    """
    basket = collections.defaultdict(int)
    left, total, result = 0, 0, 0
    for right, fruit in enumerate(fruits):
        basket[fruit] += 1
        total += 1
        while len(basket) > 2:
            f = fruits[left]
            basket[f] -= 1
            total -= 1
            left += 1
            if not basket[f]:
                basket.pop(f)
        result = max(result, total)
    return result


values = [0,1,6,6,4,4,6]
print(total_fruit(values))
