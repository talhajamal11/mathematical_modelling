# Given an array of coins and an amount, return the number of combination of coins that 
# can lead to that amount of money

def count_combination(coins: list, amount: int) -> int:
    dp = {}
    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i, a) in dp:
            return dp[i, a]
        dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return dp[(i, a)]
    return dfs(0, 0)

amount = 5
coins = [1, 2, 5]
print(count_combination(coins, amount))

def change(coins, amount):
    # Use 2D DP Array
    dp = [[0] * (len(coins) + 1) for a in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for c in range(len(coins) - 1, -1, -1):
            dp[a][c] = dp[a][c + 1]
            if a - coins[c] >= 0:
                dp[a][c] += dp[a - coins[c]][c]
    return dp[amount][0]

print(change(coins, amount))