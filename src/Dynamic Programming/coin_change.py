# Return minimum number of coins needed to get to amount
def minCoinChange(coins: list, amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):  # DP Bottom Up solution
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1 

coins = [1,2,5]
amount = 11
print(minCoinChange(coins, amount))