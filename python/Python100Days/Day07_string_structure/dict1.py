def main():
    scores = {'a': 95, 'b':79, 'c': 88}
    print(scores['a'])
    print(scores['c'])
    for elem in scores:
        print("%s\t--->\t%d" %(elem, scores[elem]))
    scores['b'] = 66
    scores['d'] = 89
    scores.update(e=88, f=66)
    print(scores)
    if 'g' in scores:
        print(scores['g'])
    print(scores.get('g'))
    print(scores.get('g', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('a', 100))
    scores.clear()
    print(scores)
    
if __name__ == '__main__':
    main()