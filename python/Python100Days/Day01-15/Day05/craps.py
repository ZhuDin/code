from random import randint

money = 1000
while money > 0:
    print('your money:', money)
    needs_go_on = False
    while True:
        debt = int(input('pay:'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('your score:%d', first)
    if first == 7 or first == 11:
        print('win!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('lose!')
        money -= debt
    else:
        needs_go_on = True
    
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('your score:%d', current)    
        if current == 7:
            print('lose!')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('win!')
            money += debt
            needs_go_on = False

print('Game over!')