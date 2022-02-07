import requests as req

r = req.get('http://www.example.com')
print((r.text)[0:300])
