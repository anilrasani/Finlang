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
raw_data.to_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv')


# 3.ploting
