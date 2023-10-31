""" 
As a first example, we consider a problem where we are given a set of coins and our task is to form a sum of money n 
using the coins. The values of the coins are coins={c1,c2,...,ck}, and each coin can be used as many times we want. 
What is the minimum number of coins needed?
For example, if the coins are the euro coins (in cents) {1, 2, 5, 10, 20, 50, 100, 200} and n = 520, 
we need at least four coins. The optimal solution is to select coins 200+200+100+20 whose sum is 520.
"""

coins = [1, 3, 4]
n = 6

def greedy_min_coins(n, coins):
    coins = sorted(coins)
    count = 0
    used = {}
    for i in range(len(coins) - 1, -1, -1):
        current_coin = coins[i]
        while n - current_coin >= 0:
            count += 1
            n -= current_coin
            used[current_coin] = 1 + used.get(current_coin, 0)
    return count

print(greedy_min_coins(n, coins))

def dp_min_coins(n, coins):
    dp = [n + 1] * (n + 1)
    dp[0] = 0
    for amount in range(1, n + 1):
        for c in coins:
            if amount - c >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - c])
    print(dp)
    return dp[n] if dp[n] != n + 1 else -1

print(dp_min_coins(n, coins))