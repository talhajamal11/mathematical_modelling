"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def greatest_common_divisor(num1: int, num2: int) -> int:
    """
    Algorithm to find the Greatest Common Divisor for two numbers

    Euclidean Algorithm:
    
    """
    while num2:
        temp = num1
        num1 = num2
        num2 = temp % num2
    return num1


def lcm(num1: int, num2: int) -> int:
    """
    Function to efficiently find LCM of two numbers

    An Efficient formula for LCM = Multiply both numbers / Their greatest common divisor
    """
    return (num1 * num2) // greatest_common_divisor(num1, num2)

print(lcm(10, 24))
