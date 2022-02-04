import requests, sys, webbrowser, bs4, logging

print('Bing...')
res = requests.get('https://www.bing.com/search?q=test')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.bing.com' + linkElems[i].get('href'))

