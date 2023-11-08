"""
Skriv en funksjon tell_forekomster(tekst) som tar inn en
tekststreng som argument og teller antall forekomster av hvert tegn
(bokstaver, tall og spesialtegn)i teksten.
Funksjonen skal returnere en fortegnelse med tegnet som
nøkkel og antall forekomster som verdi.
"""


def tell_forekomster(tekst):
    fortegnelse = dict()
    for bokstav in tekst:
        fortegnelse[bokstav] = fortegnelse.get(bokstav, 0) + 1
    return fortegnelse


# print(tell_forekomster("Hello World!"))


"""
Lag en funksjon som tar inn en tekststreng og
returnerer en fortegnelse som inneholder hvert unike ord i teksten
som nøkkel og antall forekomster av hvert ord som verdi.
"""


def tell_ord(tekst):
    tekst = tekst.split()
    fortegnelse = dict()
    for ord in tekst:
        fortegnelse[ord] = fortegnelse.get(ord, 0) + 1
    return fortegnelse


print(
    tell_ord("Dette er en test. Testen skal telle antall ganger hvert ord forekommer.")
)
