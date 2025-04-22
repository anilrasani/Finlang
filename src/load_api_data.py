# Api data
import pandas as pd 
import requests
import json

finnhub_api_key = 'cpg1ma1r01ql1vn3fk4gcpg1ma1r01ql1vn3fk50'
url=f'https://finnhub.io/api/v1/news?category=general&token={finnhub_api_key}'

response=requests.get(url)
if response.status_code ==200:
    data=response.json()
    with open(r'C:\Users\Hi\Finlang\data\api\extracted_data.json','w') as file:
        json.dump(data,file,indent=4)
    print('Json data saved succesfully.! ')
else:
    print(f'Data Failed to fetch due to {response.status_code}')
    print(response.text)

with open(r'C:\Users\Hi\Finlang\data\api\extracted_data.json','r') as file:
    news_data=json.load(file)
    data=pd.DataFrame(news_data)
    print(data.head(2))
data.to_csv(r'C:\Users\Hi\Finlang\src\data\raw\news_data.csv')
print('news_data Saved successfully..!')

# =>News-driven insight generation
