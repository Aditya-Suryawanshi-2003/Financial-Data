from Ticker import Tick, create_ticker

def get_balance_sheet(ticker: Tick, frequency: str) -> dict:
    """
    Get the balance sheet for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.
        frequency (str): The frequency of the balance sheet => “yearly” or “quarterly” or “trailing”. Default is “yearly”.

    Returns:
        dict: A dictionary containing the balance sheet information.
    """
    balance_sheet = ticker.get_balance_sheet(as_dict=True, freq=frequency)
    return balance_sheet

# itc = create_ticker("ITC.NS")
# balance_sheet = get_balance_sheet(itc, "yearly")

# print(balance_sheet)