salary = float(input('sarray: '))
insurance = float(input('insurance: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 9000:
    rate = 0.1
    deduction = 105
elif diff < 35000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505

tax = abs(diff * rate - deduction)
print('rate: $%0.2f' % tax)
print('payment: $%0.2f' % (diff + 3500 - tax))
