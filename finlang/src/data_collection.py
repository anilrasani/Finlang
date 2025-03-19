import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist

if __name__ == "__main__":
    print(get_stock_data("AAPL"))
