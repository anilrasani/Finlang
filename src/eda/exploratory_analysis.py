import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv',parse_dates=['time'])
# print(raw_data.head(10))
# print(raw_data.describe())

# Setting time as index
raw_data.set_index('time',inplace=True)
# print(raw_data)

## EDA(Ploting grapghs)

# 1.BI:
#1.should i invest now or wait?
#Ans:price trend gives a quick visual 
#1.Close: price overtime
plt.figure(figsize=(14,7))
plt.title('Close Price Overtime')
plt.xlabel('Time')
plt.ylabel('Value')
plt.plot(raw_data['close'])
plt.show()


# 2.BI:
#1.how much did my investment grow or shrink each day?
#Ans:to evalute investment performances
# 1.Daily returns
#return = (todays-yesterday)/yesterday

raw_data['Daily_returns']=raw_data['close'].pct_change()
# print(raw_data)

# Bi:
# 1.is this safe assest to hold or will it give me a heart beark?
# Ans:To ensure risk before making business
# 1.Volatitlity(std)
# high_volatility=big jumps
# low_volatality=smooth/stable

raw_data["Volatility"]=raw_data["Daily_returns"].std()
# print(raw_data["Volatility"])

# 4.avg

# high_volatile->high risk to predict
# low_volatile->stable ,consistent
# rolling volatility ->This helps see how risk changes over time.

raw_data['rolling_volatility']=raw_data['Daily_returns'].rolling(window=20).std()
# print(raw_data['rolling_volatility'])

# 5. Correlation

plt.figure(figsize=(10, 6))
sns.heatmap(raw_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

#6.Outliers 
# Boxplot for each numerical column

numerical_cols=raw_data.columns
# print(raw_data.columns)

# removing of outliers(IQR Method)

#     Q1=df['col'].quantile(0.25)
#     Q3=df['col'].quantile(0.75)
    
#     IQR=Q3-Q1

#     # define Bounds
#     lower_bound=Q1-1.5*IQR
#     upper_bound=Q3+1.5*IQR

# df_no_outliers=df[(df['col']>=lower_bound)& (df['col']<=upper_bound)]

    def remove_outliers(data,column):
        Q1=data[column].quantile(0.25)
        Q3=data[column].quantile(0.75)
        IQR=Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q1+1.5*IQR
        return data[(data[column]>=lower_bound)&(data[column]>=upper_bound)]
    
    for col in numerical_cols:
        before=raw_data.shape[0]
        no_outliers_data=remove_outliers(raw_data,col)
        after=no_outliers_data.shape[0]
        print(f'{col}: \n removed  {before-after}  outliers')
    
    no_outliers_data.to_csv(r'C:\Users\Hi\Finlang\data\processed\no_outliers_data.csv')

print('no_outliers_data saved successfully')

    
# verification for outliers
numeric_cols=no_outliers_data.columns
for col in numeric_cols:
    plt.figure(figsize=(7,7))
    sns.boxplot(data=raw_data[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

