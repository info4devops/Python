# Need to install "requests" and "chardet" modules

# Program to findout butcoin price

import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
bitcoin_info=response.json()
print('BitCoin Price as on:',bitcoin_info['time']['updated'])
print('1 BitCoin=$',bitcoin_info['bpi']['USD']['rate'])