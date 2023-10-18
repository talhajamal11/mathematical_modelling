"""
Is Possibke
"""

def isPossible(a, b, c, d):
    # Write your code here
    # Use Greatest Common Divisor
    """
    According to the definition of Greatest Common Divisior, if m is any integer, 
    then gcd(a + m * b, b) = gcd(a, b). (In this particular problem m = 1 or m = -1 
    in each step.) Therefore, the gcd of (a + b, b), (a, a + b), (a - b, b) and (a, a - b) 
    will be the same as the gcd of (a, b). Therefore, in order to move to the target point, 
    the gcd of the target point should be equal to the gcd of the starting point.
    """
    def gcd(num1, num2):
        while num2:
            temp = num1
            num1 = num2
            num2 = temp % num2
        return num1
    
    if gcd(a, b) == gcd(c, d):
        return 'Yes'
    else:
        return 'No'


a = 1
b = 4
c = 62
d = 45

print(isPossible(a,b,c,d))