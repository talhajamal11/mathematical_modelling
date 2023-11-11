"""
You are given (a, b). We can perform the following two actions:
1. a + b, b
2. a, b + a

Determine if we can get to (c, d)
"""

def gcd(num1, num2):
    while num2:
        temp = num1
        num1 = num2
        num2 = temp % num2
    return num1

def is_possible(a,b,c,d):
    print(gcd(a,b), gcd(c,d))
    if gcd(a,b) == gcd(c,d):
        return "Yes"
    else:
        return "No"


#print(is_possible(2,2,1000,998))

