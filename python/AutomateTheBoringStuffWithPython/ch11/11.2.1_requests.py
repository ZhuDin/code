import requests

res = requests.get('http://www.example.com')
print(type(res))
print(res.status_code)
print(res.text)
