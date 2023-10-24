"""
Skriv en funksjon som tar inn en liste av tall som parameter.
Funksjonen skal returnere en ny liste med kun partallene
fra den opprinnelige listen.
"""


def returner_partall(liste):
    ny_liste = list()
    for tall in liste:
        if tall % 2 == 0:
            ny_liste.append(tall)
    return ny_liste


liste = [1, 5, 4, 7, 10]
print(returner_partall(liste))
