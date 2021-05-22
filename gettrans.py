import requests
#res = requests.get('https://prettyprinted.com/doesnotexist')
res = requests.get('https://prettyprinted.com')
#print(res.status_code)
#print(res.headers)
print(res.text)

output = open('code.html','w', encoding = 'utf-8')
output.write(res.text)
output.close()

'''
if res:
	print('Response OK')
else:
	print('Response Failed')
'''
API_KEY = 'trnsl.1.1.20190415T034404Z.d77d8129886e3aa8.fe10cb47a1315f3613401fe1ed565423f23c17da'

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = dict(key=API_KEY, text='Hello', lang = 'en=es')
res = requests.get(url, params = params)
print(res.text)