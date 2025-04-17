import pandas as pd

# Crypto data

crypto_data1=pd.read_csv(r'C:\Users\Hi\Finlang\data\kaggle\Cryptocurrency Prices Dataset.csv')
print(crypto_data1.head(2))
# => for Crypto market trend analysis
#	- Analyze historical crypto trends & Sentiment vs price correlation

# Financial data
financial_data1=pd.read_csv(r'C:\Users\Hi\Finlang\data\kaggle\McDonalds_Financial_Statements.csv')
print(financial_data1.head(2))
#=>Company performance analysis

financial_data2=pd.read_csv(r'C:\Users\Hi\Finlang\data\kaggle\Financial Statements.csv')
print(financial_data2.head(2))
# =>- Benchmarking across companies & Text summarization/model training
#=>Company performance analysis

# Earnings reports
reports_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\kaggle\Employee_Earnings_Report_2016.csv')
print(reports_data.head(2))

 # => Earnings insights by job/region & Extract industry-level trends

# Stock data
stock_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\kaggle\World-Stock-Prices-Dataset.csv')
print(stock_data.head(2))

 # => Global market movement patterns & Volatility comparison
