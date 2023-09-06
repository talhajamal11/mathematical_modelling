"""
Write the below algorithms to find the square root of a number:
1. Heron Algorithm
2. Newton Rhapson Method
3. Bisection Method
4. Secant Method
"""

def square_root(number: float) -> float:
    """
    Simple way to calculate a square root of a number
    We want the answer to be close to an approximation
    """
    approximation = 0.000001
    guess = number / 2
    i = 0
    while abs(guess * guess - number) >= approximation:
        i += 1
        guess = (guess + number/guess) / 2
    return guess

# print(format(square_root(484/79), '.15f'))

def newton_raphson(function: float, derivative: float, x_0: float, tolerance = 1e-2) -> float:
    """
    finding roots
    """
    x_1 = x_0 - (function(x_0)/derivative(x_0))
    diff = abs(x_1 - x_0)
    if diff > tolerance:
        return newton_raphson(function, derivative, x_1, tolerance)
    return x_1

f = lambda x: x**3 - 100*x**2 -x + 100
f_prime = lambda x: 3*x**2 + 100*x - 1

print(format(newton_raphson(f, f_prime, 0), '.15f'))

