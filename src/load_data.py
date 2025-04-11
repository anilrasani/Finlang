import pandas as pd

raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\Data\excel_data\BTC-USD_stock_data.csv')
raw_data1=pd.read_csv(r'C:\Users\Hi\Finlang\data\Data\Stocks\a.us.txt',delimiter="\t")
print(raw_data.head(5))
print(raw_data1.head(5))
# print(raw_data.info)
# print(raw_data.columns)
# print(raw_data.dtypes)