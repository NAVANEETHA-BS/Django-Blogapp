import requests
try:
	r = requests.get('http://httpbin.org/delay/10', timeout = 5)
#except requests.exceptions.ConnectTimeout:
except requests.exceptions.ReadTimeout:

	print('TIME OUT!!!')