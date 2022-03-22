value = float(input('please enter length: '))
unit = input('please enter unit: ')
if unit == 'in' or unit == 'inch':
    print('%finch = %fcm' %(value, value*2.54))
elif unit == 'cm' or unit == 'm':
    print('%fcm = %finch' %(value, value/2.54))
else:
    print('please enter unit right.')
    