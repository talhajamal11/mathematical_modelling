"""
The Prime Factors of 13195 are 5, 7, 13, and 29

What is the largest prime factor of the number 600851475143
"""
def largest_prime_factors(num: int) -> int:
    """
    Fastest algo to find prime factor
    """
    if num == 0:
        return ValueError
    factors = {}
    prime = 2
    while num > 1:
        if num % prime == 0:
            if prime not in factors:
                factors[prime] = True
            num = num / prime
        else:
            prime += 1
    return max(factors.keys())

print(largest_prime_factors(600851475143))
