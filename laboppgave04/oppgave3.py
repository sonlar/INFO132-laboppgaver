from random import randint


def gjett_tall():
    svar = randint(1, 10)
    for x in range(3):
        gjett = int(
            input(f'Gjett et heltall mellom 1 og 10 (forsøk {x+1} av 3): '))
        if gjett > svar:
            print('For høyt')
        elif gjett < svar:
            print('For lavt')
        else:
            print('Gratulerer du gjettet riktig!')


gjett_tall()
