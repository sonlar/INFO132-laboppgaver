'''
Skriv en funksjon kalt "multiplikasjonstabell"
som tar et heltall n som argument.
Funksjonen skal skrive ut en multiplikasjonstabell
fra og med 1 til og med n. Tabellen skal se slik ut:
'''


def multiplikasjonstabell(n):
    teller = 1
    for x in range(n):
        for x in range(1, n+1):
            print(teller*x, end=' ')
        teller += 1
        print()


multiplikasjonstabell(5)
