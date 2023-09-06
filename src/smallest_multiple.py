"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def greatest_common_divisor(num1: int, num2: int) -> int:
    """
    Algorithm to find the Greatest Common Divisor for two numbers

    Euclidean Algorithm:
    Take larger problem and divide it into subproblems
    GCD(A,0) = A
    GCD(0,B) = B
    If A = B⋅Q + R (found by taking modules)
    and B≠0 then GCD(A,B) = GCD(B,R) where Q is an integer, R is an integer between 0 and B-1
    Loop until second number becomes 0, Assign second number to first number
    Assign the remainder of number1 / number 2 to number 2
    Repeat till second number = 0
    Return First Number
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

def lcm_multiple_numbers(numbers: list) -> int:
    """
    Take a list of numbers and find the LCM 
    """
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

arr = [i for i in range(1, 21)]
print(arr)
print(lcm_multiple_numbers(arr))
