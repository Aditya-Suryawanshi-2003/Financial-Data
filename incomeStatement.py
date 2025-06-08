from Ticker import Tick, create_ticker

def get_income_statement(ticker: Tick, frequency: str) -> dict:
    """
    Get the income statement for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.
        frequency (str): The frequency of the income statement => “yearly” or “quarterly” or “trailing” Default is “yearly”.

    Returns:
        dict: A dictionary containing the income statement information.
        """    
    income_statement = ticker.get_income_stmt(as_dict=True, freq=frequency)
    return income_statement

# itc = create_ticker("ITC.NS")
# income_statement = get_income_statement(itc, "yearly")
# print(income_statement)