"""
Buy Low Sell High
"""
def max_profit(array: list) -> any:
    """
    Returns Buy Date, Sell Date, and max profit
    """
    left, right = 0, 1
    profit, max_profit = 0, 0
    while right < len(array):
        # iterate over whole array
        if array[left] < array[right]:
            # profitable
            profit = array[right] - array[left]
            max_profit = max(max_profit, profit)
        else:
            # not profitable
            left = right
        right += 1
    return max_profit

prices = [1, 5, 3, 1, 8]
print(max_profit(prices))
