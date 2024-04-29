"""
This Python Script allows the user to run a Simple Factor Model to decompose the returns
of a stock into its market dependent returns and idiosyncratic returns
"""
from my_utils import download_stock_data
from my_utils import linear_regression
from my_utils import visualize_regression

SYF = download_stock_data('SYF', start='2018-01-01', end='2019-01-01')
SPY = download_stock_data('SPY', start='2018-01-01', end='2019-01-01')

regression = linear_regression(x=SPY['Daily_Ret'],
                               y=SYF['Daily_Ret'],
                               x_ticker="SPY",
                               y_ticker="SYF")

visualize_regression(SYF['Daily_Ret'],
                     SPY['Daily_Ret'],
                     regression,
                     title='SYF returns regressed on SPY returns',
                     xlabel='SPY',
                     ylabel='SYF')
