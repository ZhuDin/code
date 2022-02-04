import random

tries = 0
success = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    tries += 1
    if(x*x + y*y <= 1):
        success += 1
pi = 4 * success / tries
print(pi)
# pi = (pi*r*r)/(2*r*2*r)=pi/4