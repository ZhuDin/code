import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    print('circle: %f' % (a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('area: %f' % (area))
else:
    print('not a triangle')
    