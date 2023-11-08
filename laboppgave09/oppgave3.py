"""
Skriv en funksjon som tar inn en liste av tall som argument og
returnerer en ny liste hvor alle tallene er multiplisert med 2.

Ekstraoppgave:
Lag en variant som multipliserer med et ekstra argument faktor,
som har 2 som standardverdi.
"""


def multipliser_med_to(liste, faktor=2):
    ny_liste = list()
    for tall in liste:
        ny_liste.append(tall * faktor)
    return ny_liste


liste = [1, 5, 4, 7, 10]
print(multipliser_med_to(liste))
