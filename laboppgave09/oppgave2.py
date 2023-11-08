"""
Skriv en funksjon som tar inn en liste av tall,
og fjerner alle elementer som er mindre enn et spesifisert tall.
Den nye listen skal returneres.
"""


def fjern_mindre_enn(liste, grense):
    ny_liste = list()
    for tall in liste:
        if tall >= grense:
            ny_liste.append(tall)
    return ny_liste


liste = [1, 5, 4, 7, 10]
print(fjern_mindre_enn(liste, 4))
