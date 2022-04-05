def main():
    names = ['a', 'b', 'c', 'd', 'e']
    subjs = ['x', 'y', 'z']
    scores = [[0] * 3] * 5
    for row, name in enumerate(names):
        print('please enter %s score' % name)
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ': '))
    print(scores)

if __name__ == '__main__':
    main()
