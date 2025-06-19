from Ticker import Tick, create_ticker
import datetime

def get_prices(ticker: Tick) -> dict:
    """
    Get the current price for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the current price information.

    """
    info = ticker.data.get_info()
    price_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'Current Price': info.get('currentPrice', 'N/A'),
        'Previous Close': info.get('regularMarketPreviousClose', 'N/A'),
        'Open': info.get('regularMarketOpen', 'N/A'),
        'Day High': info.get('regularMarketDayHigh', 'N/A'),
        'Day Low': info.get('regularMarketDayLow', 'N/A')
    }
    return price_info

def get_dividend_info(ticker: Tick) -> dict:
    """
    Get the dividend information for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the dividend information.

    """
    info = ticker.data.get_info()
    dt = datetime.datetime.fromtimestamp(info.get('exDividendDate', 0))
    dividend_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'Dividend Yield': info.get('dividendYield', 'N/A'),
        'Annual Dividend Rate': info.get('dividendRate', 'N/A'),
        'Ex-Dividend Date': dt.strftime("%Y-%m-%d") if info.get('exDividendDate') else 'N/A',
        'Payout Ratio': info.get('payoutRatio', 'N/A'),
        'five_year_avg_dividend_yield': info.get('fiveYearAvgDividendYield', 'N/A'),

    }
    return dividend_info

def get_EPS_PE(ticker: Tick) -> dict:
    """
    Get the EPS and PE ratio for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the EPS and PE ratio information.

    """
    info = ticker.data.get_info()
    eps_pe_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'EPS (TTM)': info.get('trailingEps', 'N/A'),
        'PE Ratio (TTM)': info.get('trailingPE', 'N/A')
    }
    return eps_pe_info

def get_trading_info(ticker: Tick) -> dict:
    """
    Get the trading information for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the trading information.

    """
    info = ticker.data.get_info()
    trading_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'Market Cap': info.get('marketCap', 'N/A'),
        'Volume': info.get('volume', 'N/A'),
        'Average Volume': info.get('averageVolume', 'N/A'),
        'Beta': info.get('beta', 'N/A'),
        '52 Week High': info.get('fiftyTwoWeekHigh', 'N/A'),
        '52 Week Low': info.get('fiftyTwoWeekLow', 'N/A'),
        'bid': info.get('bid', 'N/A'),
        'ask': info.get('ask', 'N/A'),
        'bid size': info.get('bidSize', 'N/A'),
        'ask size': info.get('askSize', 'N/A')
    }
    return trading_info

def volatility(ticker: Tick) -> dict:
    """
    Get the volatility information for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the volatility information.

    """
    info = ticker.data.get_info()
    volatility_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        '50 Day Avg Change %': info.get('fiftyDayAverageChangePercent', 'N/A'),
        '200 Day Avg Change %': info.get('twoHundredDayAverageChangePercent', 'N/A'),
        '52 Week Change': info.get('52WeekChange', 'N/A'),
        'Beta ': info.get('beta', 'N/A'),
        '50 Day Moving Average': info.get('fiftyDayAverage', 'N/A'),
        '200 Day Moving Average': info.get('twoHundredDayAverage', 'N/A'),
        '50 Day High': info.get('fiftyDayHigh', 'N/A'),
        '50 Day Low': info.get('fiftyDayLow', 'N/A'),   
        '200 Day High': info.get('twoHundredDayHigh', 'N/A'),
        '200 Day Low': info.get('twoHundredDayLow', 'N/A'),
        '52 Week Range': f"{info.get('fiftyTwoWeekLow', 'N/A')} - {info.get('fiftyTwoWeekHigh', 'N/A')}",
        '52 Week High Change %': info.get('fiftyTwoWeekHighChangePercent', 'N/A'),
        '52 Week Low Change %': info.get('fiftyTwoWeekLowChangePercent', 'N/A'),
    }
    return volatility_info

def get_share_info(ticker: Tick) -> dict:
    info = ticker.data.get_info()
    last_split_date = info.get('lastSplitDate')
    if last_split_date and isinstance(last_split_date, (int, float)):
        dt = datetime.datetime.fromtimestamp(last_split_date)
        split_date_str = dt.strftime("%Y-%m-%d")
    else:
        split_date_str = 'N/A'
    share_info = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'Shares Outstanding': info.get('sharesOutstanding', 'N/A'),
        'Float': info.get('floatShares', 'N/A'),
        'Insider holding percentage': info.get('heldPercentInsiders', 'N/A'),
        'Institutional holding percentage': info.get('heldPercentInstitutions', 'N/A'),
        'Implied Shares Outstanding': info.get('impliedSharesOutstanding', 'N/A'),
        'bookValue': info.get('bookValue', 'N/A'),
        'priceToBook': info.get('priceToBook', 'N/A'),
        'Last splitFactor': info.get('lastSplitFactor', 'N/A'),
        'Last splitDate': split_date_str,
        'Debt to Equity': info.get('debtToEquity', 'N/A'),
        'Revenue per Share': info.get('revenuePerShare', 'N/A'),
        'Return on Assets': info.get('returnOnAssets', 'N/A'),
        'Return on Equity': info.get('returnOnEquity', 'N/A'),
    }
    return share_info


def get_financials(ticker: Tick) -> dict:
    """
    Get the financials for the given ticker.

    Args:
        ticker (Tick): An instance of the Tick class.

    Returns:
        dict: A dictionary containing the financial information.
    """
    info = ticker.data.get_info()
    financials = {
        'Ticker': ticker.ticker,
        'Company Name': info.get('longName', 'Unknown Company'),
        'Symbol': info.get('symbol', 'N/A'),
        'Total Revenue': info.get('totalRevenue', 'N/A'),
        'Gross Profit': info.get('grossProfits', 'N/A'),
        'Net Income': info.get('netIncomeToCommon', 'N/A'),
        'EBITDA': info.get('ebitda', 'N/A'),
        'Total cash': info.get('totalCash', 'N/A'),
        'Total Debt': info.get('totalDebt', 'N/A'),
        'returnOnAssets': info.get('returnOnAssets', 'N/A'),
        'returnOnEquity': info.get('returnOnEquity', 'N/A'),
        'Gross Profits': info.get('grossProfits', 'N/A'),
        'Free Cash Flow': info.get('freeCashflow', 'N/A'),
        'Operating Cash Flow': info.get('operatingCashflow', 'N/A'),
        'Earings growth': info.get('earningsGrowth', 'N/A'),
        'Revenue growth': info.get('revenueGrowth', 'N/A'),
        'Gross margin': info.get('grossMargins', 'N/A'),
        'EBITDA margin': info.get('ebitdaMargins', 'N/A'),
        'Operating margin': info.get('operatingMargins', 'N/A')
        
    }
    return financials

# itc = create_ticker('ITC.NS')  # Example ticker
# print(get_prices(itc))
# print(get_dividend_info(itc))
# print(get_EPS_PE(itc))
# print(get_trading_info(itc))
# print(volatility(itc))
# print(get_share_info(itc))
# print(get_financials(itc))