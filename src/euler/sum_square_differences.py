"""
Find the difference between the sum of the squares of the first one hundred natural numbers
 and the square of the sum.
"""

def sum_of_squares(i: int) -> int:
    """
    Return sum of squares of first i numbers
    """
    total = 0
    for num in range(1, i+1):
        total += (num)**2
    return total

def square_of_sum(i: int) -> int:
    """
    Return square of the sum of first i numbers
    """
    total = 0
    for num in range(1, i+1):
        total += num
    return total**2

print((square_of_sum(100) - (sum_of_squares(100))))
