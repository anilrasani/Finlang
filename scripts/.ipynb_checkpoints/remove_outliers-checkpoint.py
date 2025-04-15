
#6.Outliers 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load
raw_data=pd.read_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv')

# print(raw_data.dtypes)
# Get only numeric columns

numerical_cols = raw_data.select_dtypes(include=['int64', 'float64']).columns

# Boxplot for each numerical column

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


