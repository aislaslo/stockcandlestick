import yfinance as yf
import mplfinance as mpf

symbol = input("Enter stock symbol: ")
start_date = '2022-01-01'
end_date = '2025-01-01'

aapl = yf.Ticker(symbol)
stock_data = aapl.history(start=start_date, end=end_date)

mpf.plot(stock_data, type='candle', style='yahoo', title=f'{symbol} Candlestick chart')