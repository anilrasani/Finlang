import finnhub
import requests

Api_key='cpg1ma1r01ql1vn3fk4gcpg1ma1r01ql1vn3fk50'
print(Api_key)
url = "https://finnhub.io/api/v1/news?category=general&token=" + Api_key

response=requests.get(url)
if response.status_code==200:
  data=response.json()
  with open('src/data/financial_news.json','w') as file:
    json.dump(data,file,indent=4)
  print('Fianancial news data saved to src/data/financial_news.json')
else:
  print('Error on retriving the data',response.status,response.text)
