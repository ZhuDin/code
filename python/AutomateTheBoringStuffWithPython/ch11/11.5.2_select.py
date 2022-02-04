import bs4, requests

exampleFile = open('.\python\\AutomateTheBoringStuffWithPython\\ch11\\example.txt')

exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select("div")
print(type(elems))
print(len(elems))
print('\n')
print(elems[0])
print('\n')
print(elems[0].getText())
print('\n')
print(str(elems[0]))
print('\n')
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(str(pElems[0].getText()))
print(str(pElems[1]))