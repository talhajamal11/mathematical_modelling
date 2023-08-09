"""
First Six Prime Numbers: 2, 3, 5, 7, 11, 13
6th Prime Number is 13

What is the 10,001st Prime Number?
"""
def nth_prime_number(index: int) -> int:
    """
    Produces the nth Prime Number:
    My Idea here is to have an array for Prime Numbers. Each time I find a prime number, 
    I append the array. 
    Break out of the loop with a While Loop when Index has been reduced to 0
    """
    if index <= 0:
        return None
    prime = [2]
    if index == 1:
        return prime
    number = prime[-1] 
    while index > 1:
        number += 1
        prime_flag = True
        for i in range(2, number):
            if number % i == 0:
                # Not a Prime Number
                prime_flag = False
                break
        if prime_flag:
            prime.append(number)
            index -= 1
    return prime[-1]

print(nth_prime_number(10001))
