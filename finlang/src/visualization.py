import matplotlib.pyplot as plt
import seaborn as sns
from data_collection import get_stock_data

def plot_stock_trend(ticker):
    df = get_stock_data(ticker)
    plt.figure(figsize=(10,5))
    sns.lineplot(data=df, x=df.index, y="Close", label="Close Price")
    plt.title(f"{ticker} Stock Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_stock_trend("AAPL")

