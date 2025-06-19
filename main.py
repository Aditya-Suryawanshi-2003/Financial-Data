import sys
import traceback
import logging

# # Configure logging first
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
#     handlers=[
#         logging.StreamHandler(sys.stderr)
#     ]
# )

# logger = logging.getLogger("yahoo_finance_mcp")

# def handle_exception(exc_type, exc_value, exc_traceback):
#     # logger.error("Uncaught Exception:", exc_info=(exc_type, exc_value, exc_traceback))
#     traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)

# sys.excepthook = handle_exception

try:
    # logger.info("Starting imports...")
    from mcp.server.fastmcp import FastMCP # type: ignore
    # logger.info("FastMCP imported successfully")
    
    import financials # type: ignore
    # logger.info("financials imported successfully")
    
    import balanceSheet
    # logger.info("balanceSheet imported successfully")
    
    import incomeStatement
    # logger.info("incomeStatement imported successfully")
    
    from Ticker import Tick, create_ticker
    # logger.info("Ticker imported successfully")
    
    from companyNameSymbol import list_of_name_symbols
    # logger.info("companyNameSymbol imported successfully")
    
    # logger.info("All imports completed successfully")
    
except ImportError as e:
    # logger.error(f"Import error: {e}")
    sys.exit(1)
except Exception as e:
    # logger.error(f"Unexpected error during imports: {e}")
    sys.exit(1)

# logger.info("Initializing server...")
mcp = FastMCP("yahoo_finance_mcp")

# @mcp.tool()
# def get_company_name_symbols() -> dict:
#     """
#     Returns a dict of company names and corresponding yfinance symbols.
#     """
#     try:
#         return list_of_name_symbols()
#     except Exception as e:
#         # logger.error(f"Error in get_company_name_symbols: {e}")
#         raise

@mcp.tool()
def stock_price(ticker: str) -> dict:
    """
    Get the stock price for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the stock price information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_prices(tick)
    except Exception as e:
        # logger.error(f"Error in stock_price for {ticker}: {e}")
        raise

@mcp.tool()
def dividend_info(ticker: str) -> dict:
    """
    Get the dividend information for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the dividend information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_dividend_info(tick)
    except Exception as e:
        # logger.error(f"Error in dividend_info for {ticker}: {e}")
        raise

@mcp.tool()
def eps_pe(ticker: str) -> dict:
    """
    Get the EPS and PE ratio for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the EPS and PE ratio information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_EPS_PE(tick)
    except Exception as e:
        # logger.error(f"Error in eps_pe for {ticker}: {e}")
        raise

@mcp.tool()
def trading_info(ticker: str) -> dict:
    """
    Get the trading information for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the trading information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_trading_info(tick)
    except Exception as e:
        # logger.error(f"Error in trading_info for {ticker}: {e}")
        raise

@mcp.tool()
def volatilet_info(ticker: str) -> dict:
    """
    Get the volatility information for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the volatility information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.volatility(tick)
    except Exception as e:
        # logger.error(f"Error in volatilet_info for {ticker}: {e}")
        raise

@mcp.tool()
def share_info(ticker: str) -> dict:
    """
    Get the share information for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the share information.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_share_info(tick)
    except Exception as e:
        # logger.error(f"Error in share_info for {ticker}: {e}")
        raise

@mcp.tool()
def get_financials_tool(ticker: str) -> dict:
    """
    Get the financials for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the financials.
    """
    try:
        tick = create_ticker(ticker)
        return financials.get_financials(tick)
    except Exception as e:
        # logger.error(f"Error in financials for {ticker}: {e}")
        raise

@mcp.tool()
def balance_sheet(ticker: str, frequency: str) -> dict:
    """
    Get the balance sheet for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.
        frequency (str): The frequency of the balance sheet => "yearly" or "quarterly" or "trailing". Default is "yearly".

    Returns:
        dict: A dictionary containing the balance sheet information.
    """
    try:
        tick = create_ticker(ticker)
        return balanceSheet.get_balance_sheet(tick, frequency)
    except Exception as e:
        # logger.error(f"Error in balance_sheet for {ticker}: {e}")
        raise

@mcp.tool()
def income_statement(ticker: str, frequency: str) -> dict:
    """
    Get the income statement for the given ticker.

    Args:
        ticker (str): The stock ticker symbol.
        frequency (str): The frequency of the income statement => "yearly" or "quarterly" or "trailing". Default is "yearly".

    Returns:
        dict: A dictionary containing the income statement information.
    """
    try:
        tick = create_ticker(ticker)
        return incomeStatement.get_income_statement(tick, frequency)
    except Exception as e:
        # logger.error(f"Error in income_statement for {ticker}: {e}")
        raise


if __name__ == "__main__":
    # logger.info("Script starting...")
    try:
        # logger.info("Running the MCP server...")
        mcp.run()
    except Exception as e:
        # logger.error(f"Exception in main execution: {e}")
        traceback.print_exc()
        sys.exit(1)