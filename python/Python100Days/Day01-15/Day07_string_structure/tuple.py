def main():
    t = ('be', 31, True, 'EE')
    print(t)
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])

    for member in t:
        print(member)

    t = ('zone', 18, True, 'AA')
    print(t)
    person = list(t)
    print(person)
    person[0] = 'Lee'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])

if __name__ == '__main__':
    main()
