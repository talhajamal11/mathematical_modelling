"""
Buy Low Sell High
"""
prices = [1, 5, 3, 1, 8]

def max_profit(array: list) -> any:
    """
    Returns Buy Date, Sell Date, and max profit
    """
    left, right = 0, 1 # left = buy, right = sell
    profit = 0
    buy, sell = 0, 0
    while right < len(array):
        # Check for max profit
        if array[left] < array[right]:
            # profitable
            # is current profit higher than existing profit?
            profit = max(profit, array[right] - array[left])
            buy = array[left]
            sell = array[right]
        elif array[right] < array[left]:
            # current price is lower - buy low
            left = right
        right += 1
    return profit, buy, sell

print(max_profit(prices))
