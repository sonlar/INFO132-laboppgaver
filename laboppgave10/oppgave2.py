"""
Skriv en funksjon hent_snittkarakterer(karakterer)
som tar inn en liste med tupler,
der hver tuppel inneholder navn på studenten og karakterene dens.
Funksjonen skal beregne gjennomsnittskarakteren og returnere denne.
"""


def hent_snittkarakterer(karakterer):
    snitt = []
    for navn, karakter in karakterer:
        snitt.append(karakter)
    return sum(snitt) / len(snitt)


print(hent_snittkarakterer([("Alice", 3), ("Bob", 4), ("Charlie", 5)]))
