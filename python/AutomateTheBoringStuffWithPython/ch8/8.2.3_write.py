baconFile = open('.\python\\AutomateTheBoringStuffWithPython\\test\\bacon.txt','w')

baconFile.write('hello world!\n')
baconFile.close()

baconFile = open('.\python\\AutomateTheBoringStuffWithPython\\test\\bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('.\python\\AutomateTheBoringStuffWithPython\\test\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
