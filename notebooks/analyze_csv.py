import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1.Loading & exploring

raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\ada.csv',parse_dates=['time'])
# print(df.head(5))

# 2.setting indexing to df

raw_data.set_index('time',inplace=True)
print(raw_data.head(5))

# print(raw_data.info)
# print(raw_data.dtypes)
# print(raw_data.columns)

# removing unwanted spaces in cols
raw_data.columns=raw_data.columns.str.strip()

# print(raw_data.columns)
raw_data.to_csv(r'C:\Users\Hi\Finlang\data\cleaned_data.csv')
# 3.ploting

#1.plot Close over time

plt.plot(raw_data['close'],label='Close')
plt.ylabel('Close')
plt.xlabel('Time')
plt.title('Close over time')
# plt.show()
#2.Returns
    # return = (todays price-yesterday price)/yesterday price
    
    # Daily_returns=raw_data['close'].pct_change()
raw_data['Daily_returns']=raw_data['close'].pct_change()
# print(raw_data['Daily_returns'])

#3.Volatile

raw_data['volatile']=raw_data['Daily_returns'].std()
# raw_data['volatile']
raw_data['rolling_volatile']=raw_data['Daily_returns'].rolling(window=20).std()
#raw_data['rolling_volatile']
#4.MA/Support/Resistance

plt.figure(figsize=(12,7))
plt.plot(raw_data.index,raw_data['rolling_volatile'],color="purple")
plt.title('Price stability')
plt.xlabel('time')
plt.ylabel('volatility')
plt.grid(True)

plt.show()

