import requests
'''
r = requests.get('http://httpbin.org/status/500')
try:
	r.raise_for_status()
except requests.exceptions.HTTPError:
	print('ERROR! ERROR! ERROR!')
print(r)
'''

try:
	r = requests.get('https://bvdhsbghgfh.com')
except requests.exceptions.ConnectionError: 
	print('CONNECTION ERROR!')