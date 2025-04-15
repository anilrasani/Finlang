# 6. Outliers
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
raw_data = pd.read_csv(r'C:\Users\Hi\Finlang\data\processed\cleaned_data.csv')

# Get only numeric columns
numerical_cols = raw_data.select_dtypes(include=['int64', 'float64']).columns

# Function to remove outliers using IQR method
def remove_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Apply outlier removal column by column
for col in numerical_cols:
    before = raw_data.shape[0]
    raw_data = remove_outliers(raw_data, col)
    after = raw_data.shape[0]
    print(f'{col}: removed {before - after} outliers')

# Save the data after outlier removal
raw_data.to_csv(r'C:\Users\Hi\Finlang\data\processed\no_outliers_data.csv', index=False)
print('no_outliers_data saved successfully')

# Visual verification using boxplots
for col in numerical_cols:
    plt.figure(figsize=(7, 5))
    sns.boxplot(y=raw_data[col])
    plt.title(f'Boxplot of {col} (After Outlier Removal)')
    plt.tight_layout()
    plt.show()
