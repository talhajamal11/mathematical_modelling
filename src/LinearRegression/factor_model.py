"""
This Python Script allows the user to run a Simple Factor Model to decompose the returns
of a stock into its market dependent returns and idiosyncratic returns
"""
from my_utils import download_stock_data
from my_utils import linear_regression
from my_utils import visualize_regression

START = '2015-01-01'
END = '2019-01-01'

SPY = download_stock_data('SPY', start=START, end=END)

"""
visualize_regression(SYF['Daily_Ret'],
                     SPY['Daily_Ret'],
                     regression,
                     title='SYF returns regressed on SPY returns',
                     xlabel='SPY',
                     ylabel='SYF')
"""

TSLA = download_stock_data('TSLA', start=START, end=END)

tsla_regression = linear_regression(x=SPY['Daily_Ret'],
                                    y=TSLA['Daily_Ret'],
                                    x_ticker="SPY",
                                    y_ticker="TSLA")

WMT = download_stock_data('WMT', start=START, end=END)
wmt_regression = linear_regression(x=SPY['Daily_Ret'],
                                   y=WMT['Daily_Ret'],
                                   x_ticker="SPY",
                                   y_ticker="WMT")
