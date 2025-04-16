import pandas as pd
# 1.Loadind data
raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\BTC-USD_stock_data.csv')
# raw_data1=pd.read_csv(r'C:\Users\Hi\Finlang\data\Data\Stocks\a.us.txt',delimiter="\t")
print(raw_data.head(5))
# print(raw_data1.head(5))
# print(raw_data.info)
# print(raw_data.columns)
# print(raw_data.dtypes)
# print(raw_data.describe())

# 2.setting indexing to df

raw_data.set_index('time',inplace=True)


3.# removing unwanted spaces in cols
raw_data.columns=raw_data.columns.str.strip()

4.# print(raw_data.columns)
raw_data.to_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv')
