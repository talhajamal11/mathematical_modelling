"""
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2**2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?

Design Thoughts:
- One function to calculate prime factorisation of a number
    - Enhance the function to find if the prime numbers are four distinct
        - if yes, append it to a list or hashmap. 
            - After adding, check if there are more than one members in the list, if there are
              check if the numbers are consecutive, if yes, go ahead with the loop, otherwise
              empty the hashmap keys or list
            - once the list or hashmap grows to three 
"""
def prime_factorisation(num: int) -> list:
    """
    This function should take a number input and return a list containing the distinct prime factors
    """
    if num == 1:
        return [1]
    factors = []
    prime = 2
    while num != 1:
        if num % prime == 0:
            # Prime is a factor
            factors.append(prime)
            num = num / prime
        else:
            prime += 1
    return factors

# for i in range(1, 16):
#     print(f'The Prime Factors for {i} are {prime_factorisation(i)}')


