import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please enter:'))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print('right!')
        break
print('guess %d times' % counter)
if counter > 7:
    print('do more exercise')
    