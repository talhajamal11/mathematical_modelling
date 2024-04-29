"""This utils file contains the helper functions needed for Linear Regression
"""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def download_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """ Download Stock Data

    Args:
        ticker (str): Ticker
        start (str): Date Format %Y-%m-%d
        end (str): Date Format %Y-%m-%d

    Returns:
        pd.DataFrame: Dataframe with data for the stock
    """
    data = yf.download(ticker, start=start, end=end)
    data['Date'] = data.index
    data['Daily_Ret'] = data['Adj Close'].pct_change()
    data.dropna(inplace=True)
    print(f"------ Downloaded data for {ticker} --------")
    return data

def linear_regression(x: pd.Series, y: pd.Series, x_ticker: str, y_ticker: str) -> LinearRegression:
    """ Function to run a Linear Regression

    Args:
        x (pd.Series): The Independent Variable
        y (pd.Series): The Dependent Variable
        x_ticker (str): Ticker for X
        y_ticker(str): Ticker for Y

    Returns:
        LinearRegression: Returns the LR Model and prints the regression coefficients
    """
    X = np.array(x).reshape(-1, 1)
    Y = np.array(y)
    model = LinearRegression()
    model.fit(X, Y)
    prediction = model.predict(X)
    results = {
        "model":model,
        "prediction":prediction,
        "intercept":model.intercept_,
        "coefficient":model.coef_,
        "mse":mean_squared_error(Y, prediction)
    }
    print("--------------------")
    print("Regression Results:")
    print(f"{y_ticker} = {round(model.intercept_, 4)} + {round(model.coef_[0], 4)} x {x_ticker}")
    print(f"Alpha = {round(model.intercept_, 4)}")
    print(f"Beta = {round(model.coef_[0], 4)}")
    return results

def visualize_regression(stock: pd.Series, market:pd.Series, regression: list,
                         title: str, xlabel: str, ylabel: str) -> plt.figure:
    """ Create a Plot to visualize the line of best fit

    Args:
        stock (pd.Series): The Stock Returns Series
        market (pd.Series): The Market Returns Series
        regression (list): Regression Model Prediction List
        title (str): Title of the Plot
        xlabel (str): X Axis Label
        ylabel (str): Y Axis Label

    Returns:
        plt.figure: Figure Showing the Regression Line of Best Fit
    """
    X = np.array(market)
    Y = np.array(stock)
    y_hat = np.array(regression['prediction'])
    plt.figure(figsize=(8,5))
    plt.scatter(X, Y)
    plt.plot(X, y_hat, color='red', label='Regression Results')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    return plt.figure
