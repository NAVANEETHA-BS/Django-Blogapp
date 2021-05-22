import requests
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#print('The current price of bitcoin is: $' + r.json()['bpi']['USD']['rate'])
print(r.json()['bpi']['USD']['rate'])