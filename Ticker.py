import yfinance as yf # type: ignore
import numpy as np
import pandas as pd
class Tick(yf.Ticker):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.ticker = ticker
        self.data = yf.Ticker(ticker)
        self.company_name = self.data.info.get('longName', 'Unknown Company')
        

def create_ticker(ticker: str) -> Tick:
    """
    Create a ticker object for the given ticker symbol.
    
    Args:
        ticker (str): The ticker symbol to create the object for.
        
    Returns:
        Tick: An instance of the Tick class with the specified ticker.

    """
    tikr = Tick(ticker)
    return tikr

