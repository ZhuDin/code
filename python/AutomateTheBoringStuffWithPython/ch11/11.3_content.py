import requests

res = requests.get('http://www.example.com')
print(res.raise_for_status())
playFile = open('.\python\\AutomateTheBoringStuffWithPython\\ch11\\example.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

playFile.close()
