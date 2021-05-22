import requests
payload = {'first_name' : 'neetha', 'last_name' : 'developer'}
r = requests.post('http://reqres.in/api/users?page=2', json = payload)
print(r)
print(r.text)
