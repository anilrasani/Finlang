import finnhub
import requests

Api_key='cpg1ma1r01ql1vn3fk4gcpg1ma1r01ql1vn3fk50'
print(Api_key)
URL = "https://finnhub.io/api/v1/news?category=general&token=" + API_KEY

response=requests.get(url)
if response.status==200:
  data=response.json()
  print(data[:3])
else:
  print('Error on retriving the data',response.status,response.text)
