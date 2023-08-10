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
- One function to calculate prime numbers
    - Enhance the function to find if the prime numbers are four distinct
        - if yes, append it to a list or hashmap. 
            - After adding, check if there are more than one members in the list, if there are
              check if the numbers are consecutive, if yes, go ahead with the loop, otherwise
              empty the hashmap keys or list
            - once the list or hashmap grows to three 
"""
