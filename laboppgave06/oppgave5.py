
'''
Lag en Python-funksjon som tar inn en streng som input og
returnerer en ny streng hvor alle vokalene (a, e, i, o, u)
er erstattet med stjernetegnet "*" (asterisk).
Funksjonen skal bruke string-modulen til å definere vokalene og
deretter utføre erstatningen.
'''
tekst = 'ahei på deg'


def erstatt_vokaler(tekst):
    ny_tekst = tekst
    vokaler = 'aeiou'
    for vokal in vokaler:
        if vokal in tekst:
            ny_tekst = ny_tekst.replace(vokal, '*')
    print(f'{ny_tekst}')


erstatt_vokaler(input)
