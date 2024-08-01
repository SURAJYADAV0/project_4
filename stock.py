import yfinance as yf
import pandas as pd

def fetch_yahoo_finance_data(symbol, start_date, end_date):
    try:
        df = yf.download(symbol, start=start_date, end=end_date, interval='1d')
        if df.empty:
            print(f"No data found for {symbol}")
            return None
        df.reset_index(inplace=True)
        df.rename(columns={
            'Date': 'Date',
            'Open': 'Open',
            'High': 'High',
            'Low': 'Low',
            'Close': 'Close',
            'Volume': 'No. of Shares'
        }, inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def save_stock_data(symbols, start_date, end_date):
    for symbol in symbols:
        df = fetch_yahoo_finance_data(symbol, start_date, end_date)
        
        if df is not None:
            df.to_csv(f"{symbol}_stock_data_2019_2020.csv", index=False)
            print(f"Data for {symbol} saved to {symbol}_stock_data_2019_2020.csv")
        else:
            print(f"Failed to fetch or save data for {symbol}")

# Example usage
symbols = ["RELIANCE.BO", "TCS.BO", "INFY.BO", "HDFCBANK.BO"]  # Updated ticker symbols
start_date = "2019-01-01"
end_date = "2020-12-31"
save_stock_data(symbols, start_date, end_date)
