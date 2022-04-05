def main():
    number = int(input('please enter num: '))
    names = [None] * number
    scores = [None] * number
    for index in range(len(names)):
        names[index] = input('please enter %dth name: ' %(index+1))
        scores[index] = float(input('please enter %dth score:' %(index+1)))
    total = 0
    for index in range(len(names)):
        print('%s: %.1f' % (names[index], scores[index]))
        total += scores[index]
    print('average scores: %.1f' % (total/number))

if __name__ == '__main__':
    main()
