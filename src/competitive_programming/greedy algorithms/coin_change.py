""" 
As a first example, we consider a problem where we are given a set of coins and our task is to form a sum of money n 
using the coins. The values of the coins are coins={c1,c2,...,ck}, and each coin can be used as many times we want. 
What is the minimum number of coins needed?
For example, if the coins are the euro coins (in cents) {1, 2, 5, 10, 20, 50, 100, 200} and n = 520, 
we need at least four coins. The optimal solution is to select coins 200+200+100+20 whose sum is 520.
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 520

def min_coins(n, coins):
    coins = sorted(coins)
    count = 0
    used = {}
    for i in range(len(coins) - 1, -1, -1):
        while n - coins[i] > 0:
            count += 1
            n -= coins[i]
            used[coins[i]] = 1 + used.get(coins[i], 0)
    return count

print(min_coins(n, coins))

