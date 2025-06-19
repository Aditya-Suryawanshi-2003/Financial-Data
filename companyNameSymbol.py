from Ticker import Tick, create_ticker
import pandas as pd


def list_of_name_symbols():
    """
    Returns a dict of company names and corresponding yfinance symbols from the symbols.csv file.
    """
    df = pd.read_csv('symbols.csv')
    df['Symbol'] = df['Symbol'] + '.NS'
    return dict(zip(df['Company Name'], df['Symbol']))

