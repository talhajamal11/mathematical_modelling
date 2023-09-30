"""
Max Zeros between two ones
"""

def max_zeros(N):
    """
    return max zeros
    """
    num = bin(N)[2:]
    n = len(num)
    max_zeros = 0
    left, right = 0, 0
    bool_first_one = False

    if n  == 0:
        return n

    for index, num in enumerate(num):
        # Find the first 1
        if bool_first_one is False and num == '1':
            bool_first_one = True
            left = index
            right = index
        elif bool_first_one is True and num == '0':
            right += 1
        elif bool_first_one is True and num == '1':
            max_zeros = max(max_zeros, right - left)
            left = index
            right = index
            
    return max_zeros

print(max_zeros(1041))
