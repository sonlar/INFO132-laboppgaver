import random


def eightball(svar):
    input('Hva vil du spørre 8-ball om? ')
    if svar == 1:
        print('ja')
    elif svar == 2:
        print('nei')
    else:
        print('kanskje')


eightball(random.randint(1, 3))
