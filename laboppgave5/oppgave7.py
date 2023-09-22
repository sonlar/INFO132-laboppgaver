'''
Denne oppgaven ligner på oppgave 3 i lab 4, men her skal man bruke løkker,
og funksjonen skal kjøre fram til man har gjettet riktig.

Skriv en funksjon kalt "gjette_tall" som tar inn et tilfeldig tall
mellom 1 og 100, og lar brukeren gjette tallet.
Hvis brukeren gjetter riktig, skal funksjonen skrive ut
"Gratulerer, du gjettet riktig!" og antall forsøk det tok.
Hvis brukeren gjetter feil,
skal funksjonen gi hint om tallet er høyere eller lavere,
og la brukeren gjette på nytt.
Programmet skal avsluttes når brukeren treffer riktig tall.
'''


from random import randint


def gjette_tall(tall):
    gjett = 0
    teller = 0
    print(tall)
    while gjett != tall:
        gjett = int(input('Gjett et tall mellom 1-100: '))
        teller += 1
        if gjett > tall:
            print('For høyt!')
        elif gjett < tall:
            print('For lavt!')
    print(f'Gratulerer, du gjettet riktig! Det tok deg {teller} forsøk.')


gjette_tall(randint(1, 100))
