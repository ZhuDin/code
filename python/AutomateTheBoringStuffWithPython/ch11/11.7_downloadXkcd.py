import requests, bs4, os

url = 'https://www.bing.com'
os.makedirs('images', exist_ok=True)

while not url.endswith('/html>'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#image')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status
        imageFile = open(os.path.join('.\python\\AutomateTheBoringStuffWithPython\\ch11\\image-', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()

print('Done.')