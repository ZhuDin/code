import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo1.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
