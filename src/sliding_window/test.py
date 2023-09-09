"""
Buy Low Sell High
"""

prices = [7, 3, 1, 5, 3]

def max_profit(arr: list) -> any:
    """
    return max profit
    """
    left, right = 0, 1 # Two pointers, left = buy, right = sell
    max_profit = 0
    while right < len(arr):
        if arr[left] < arr[right]:
            # profitable
            # calculate max profit
            profit = arr[right] - arr[left] # current profit
            max_profit = max(max_profit, profit) # max profit
        else:
            # not profitable
            # buy at lower price
            left = right
        right += 1
    return max_profit

print(max_profit(prices))
