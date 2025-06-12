import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period='6mo', interval='1d'):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

def add_moving_averages(df, windows=[20, 50]):
    for window in windows:
        df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df
