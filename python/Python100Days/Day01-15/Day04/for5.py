x = int(input('x='))
y = int(input('y='))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d and %d greatest common divisor is %d' % (x,y,factor))
        print('%d and %d least common multiple is %d' % (x,y, x*y//factor))
        break