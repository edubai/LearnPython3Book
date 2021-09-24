""" A python program that looks up bitcoin price from
coindesk website api """


import requests

ETHEREUM_PRICE = 0
POLKADOT_PRICE = 0
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_price = data["bpi"]["USD"]["rate"]
_type = type(data)
print(f"{bitcoin_price} and {_type}")
