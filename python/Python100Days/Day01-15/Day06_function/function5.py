def f1(a, b=5, c=10):
    return a+b*2+c*3

print(f1(1,2,3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2,b=3,a=1))

def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1,2,3))
print(f2(1,2,3,4,5))
print(f2())

def f3(**kw):
    if 'name' in kw:
        print('welcome %s' % kw['name'])
    elif 'tel' in kw:
        print('phone: %s!' % kw['tel'])
    else:
        print('no info!')

param = {'name': 'zd', 'age': 31}
f3(**param)
f3(name='zd', age=31, tel='xxx33557799')
f3(user='zd', age=31, tel='xxx33557799')
f3(user='zd', age=31, mobile='xxx335599')
