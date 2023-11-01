""" 
calculate the total number of ways to produce a sum x using the coins. 
For example, if coins = {1, 3, 4} and x = 5, there are a total of 6 ways:
"""

def ways_coins(n, coins):
    count = [0] * (n + 1)
    count[0] = 1
    for x in range(1, n + 1):
        for c in coins:
            if x - c >= 0:
                count[x] += count[x - c]
    return count[n]

print(ways_coins(n=5, coins=[1, 3, 4]))