import requests, bs4

res = requests.get('http://www.example.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))
