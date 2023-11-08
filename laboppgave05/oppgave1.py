'''
Skriv en funksjon som tar inn to heltall: start og slutt.
Funksjonen skal skrive ut alle tallene fra og med start
til og med slutt ved hjelp av en "for"-løkke.
'''


def skriv_tall(x, y):
    for i in range(x, y+1):
        print(x)
        x += 1


skriv_tall(3, 7)
