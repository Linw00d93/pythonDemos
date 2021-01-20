import requests

url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&&apikey="

response = requests.request("GET" , url)
data = response.json()
print(data)
stock = data["Global Quote"]["01. symbol"]
currentPrice =  data["Global Quote"]["02. open"]
recentHigh = data["Global Quote"]["03. high"]
recentLow =  data["Global Quote"]["04. low"]
lastestChange =  data["Global Quote"]["09. change"]
print (stock,currentPrice,recentHigh,recentLow,lastestChange)

#stock
#symbol
#high
#low
#price
#change
