"""
Buy Low Sell High
"""
input = [7, 1, 5, 3, 6, 4]

def max_profit(array: list) -> any:
    """
    Returns Buy Date, Sell Date, and max profit
    """
    l, r = 0, 1 # left = buy, right = sell 
    while r <= len(array):
        # Check for max profit
        

