import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv')
raw_data.head(5)
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

# Only keep numeric columns for correlation
numeric_data = raw_data.select_dtypes(include=['float64', 'int64'])

#5 .HeatMap for Correlation
import seaborn as sns
 
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()