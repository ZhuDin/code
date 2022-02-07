from difflib import HtmlDiff
import urllib
response = urllib.request.urlopen('http://www.example.com')

html = response.info()
print(html)