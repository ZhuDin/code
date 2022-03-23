str1 = 'hello, world!'
print('str length:', len(str1))
print('str Title:', str1.title())
print('str upper:', str1.upper())
print('is str upper:', str1.isupper())
print('start with hello:', str1.startswith('hello'))
print('end with hello:', str1.endswith('hello'))
print('start with !:', str1.startswith('!'))
print('end with !:', str1.endswith('!'))

str2 = '- \u5b22\u373c'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
