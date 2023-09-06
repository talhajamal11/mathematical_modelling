"""
Write the below algorithms to find the square root of a number:
1. Heron Algorithm
2. Newton Rhapson Method
3. Bisection Method
4. Secant Method
"""
def square_root(number: float, tolerance = 1e-2) -> float:
    """
    Simple way to calculate a square root of a number
    We want the answer to be close to an approximation
    """
    guess = number / 2
    i = 0
    while abs(guess * guess - number) >= tolerance:
        i += 1
        guess = (guess + number/guess) / 2
    return guess

print(format(square_root(37), '.15f'))


def newton_raphson(function: float, derivative: float, x_0: float, tolerance = 1e-2) -> float:
    """
    finding roots
    """
    x_1 = x_0 - (function(x_0)/derivative(x_0))
    diff = abs(x_1 - x_0)
    if diff > tolerance:
        return newton_raphson(function, derivative, x_1, tolerance)
    return x_1

f = lambda x: 37 - x**2
f_prime = lambda x: -2*x

print(format(newton_raphson(f, f_prime, 6), '.15f'))


def bisection(number:int, tolerance=1e-2) -> float:
    """
    Using a bisection technique to find the root
    """
    low = 0
    high = max(1, number)
    guess = (low + high) / 2
    while abs(guess**2 - number) >= tolerance:
        if guess**2 > number:
            high = guess # update high
        else:
            low = guess # update low
        guess = (low + high) / 2
    return guess

print(format(bisection(37), '.15f'))
