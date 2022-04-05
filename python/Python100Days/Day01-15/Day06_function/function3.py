def myfilter(mystr):
    return len(mystr) == 6

print(chr(0x1145))
print(hex(ord('A')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345,5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1,3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)
