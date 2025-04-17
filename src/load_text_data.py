import pandas as pd
import requests



# data1=pd.read_csv(r'C:\Users\Hi\Finlang\data\yahoo\company_esg_financial_dataset.csv')
# print(data1.head(5))

# ==============================================================================

import pandas as pd
import requests
import json
import os

# Step 1: Set your Finnhub API key
finnhub_api_key = 'cpg1ma1r01ql1vn3fk4gcpg1ma1r01ql1vn3fk50'

# Step 2: Create the news endpoint URL
url = f'https://finnhub.io/api/v1/news?category=general&token={finnhub_api_key}'

# Step 3: Send the request
response = requests.get(url)

# Step 4: If request is successful, save the data
if response.status_code == 200:
    data = response.json()

    # Step 5: Make sure the folder exists
    os.makedirs("data/raw/newsapi", exist_ok=True)

    # Step 6: Save the JSON file
    with open("data/raw/newsapi/financial_news.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ News data saved successfully!")
else:
    print(f"❌ Error fetching data: {response.status_code}")
    print(response.text)

# Step 7: Load the saved JSON into a Pandas DataFrame
with open("data/raw/newsapi/financial_news.json", "r") as f:
    news_data = json.load(f)

# Step 8: Convert to DataFrame and display
df_news = pd.DataFrame(news_data)
print(df_news[['datetime', 'headline', 'summary']].head())
