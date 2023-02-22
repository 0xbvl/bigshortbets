import requests
import time

contractAddress = '0x131157c6760f78f7ddf877c0019eba175ba4b6f6'
## checkAnyContract = input('enter contract address: ')

url1 = f'https://api.ethplorer.io/getTokenInfo/{contractAddress}?apiKey=freekey'
url2 = f'https://api.ethplorer.io/getTopTokenHolders/{contractAddress}?apiKey=freekey&limit=20'
response1 = requests.get(url1)
response2 = requests.get(url2)

var1 = response1.json()
var2 = response2.json()


price1 = round(float(var1['price']['rate']), 2)
time.sleep(3)
marketcap1 = round(float(var1['price']['marketCapUsd']), 2)
volume24h1 = round(float(var1['price']['volume24h']), 2)
decimals1 = int(var1['decimals'])
totalSupply1 = round(float(var1['totalSupply']) / 1000000000000000000, decimals1)

i = 0

print('\n' + 'Name: ', var1['name'])
print('Symbol: ', var1['symbol'])
print('Contract address: ', var1['address'])
print('Total Supply: ', totalSupply1)
print('Holders: ', var1['holdersCount'])
print('Transfers: ', var1['transfersCount'])
print('Price: ', price1, 'USD')
print('Market Capitalization: ', marketcap1, 'USD')
print('Volume 24h : ', volume24h1, 'USD' + '\n')

print('Top 20 Holders: ')
for i in range(0,20):
    print(var2['holders'][i]['address'], 'have:', var2['holders'][i]['share'], '%')
