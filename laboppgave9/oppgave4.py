"""
Skriv en funksjon som tar inn to lister med tall som parametere.
Funksjonen skal returnere en ny liste som inneholder tallene
som er felles for begge listene, uten duplikater.
"""


def felles_tall(liste1, liste2):
    ny_liste = list()
    for tall in liste1:
        if tall in liste2:
            ny_liste.append(tall)
    return ny_liste


def felles_tall_set(liste1, liste2):
    set1 = set(liste1)
    set2 = set(liste2)
    return set1.intersection(set2)


liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
print(felles_tall(liste1, liste2))
print(felles_tall_set(liste1, liste2))
