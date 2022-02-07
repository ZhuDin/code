import urllib3
http = urllib3.PoolManager()

resp = http.request('GET', 'http://www.example.com')
print(resp.data)