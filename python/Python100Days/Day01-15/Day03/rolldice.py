from random import randint

face = randint(1, 6)
if face == 1:
    result = 'singing'
elif face == 2:
    result = 'dance'
elif face == 3:
    result = 'shoot'
elif face == 4:
    result = 'excise'
elif face == 5:
    result = 'tictok'
else:
    result = 'joke'

print(result)
