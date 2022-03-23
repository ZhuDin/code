num = int(input('please enter integer:'))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp%10
    temp //= 10
if num == num2:
    print('%d is palindrome' % num)
else:
    print('%d is not palindrome' % num)
