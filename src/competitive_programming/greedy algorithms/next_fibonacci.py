""" 
Given a Fibonacci Sequence number, find the next number
"""
import numpy as np

def next_fib(n):
    num1 = (1/2) * (n + np.sqrt(5 * n**2 + 4))
    num2 = (1/2) * (n + np.sqrt(5 * n**2 + 4))
    if type(int(num1)) == int:
        return int(num1)
    else:
        return int(num2)
