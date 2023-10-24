"""
Skriv en funksjon som tar inn en liste av strenger og
returnerer en ny liste der strengene er sortert alfabetisk,
uten å bruke en innebygget Python-funksjon (som sort() eller sorted()).
"""


def sorter_liste_alfabetisk(liste):
    ny_liste = list()
    for item in liste:
        if len(ny_liste) != 0 and item < ny_liste[-1]:
            for index in range(len(ny_liste)):
                if item < ny_liste[index]:
                    ny_liste.insert(index, item)
                    break
        else:
            ny_liste.append(item)

    return ny_liste


liste = ["Python", "Java", "C++", "Ruby"]
print(sorter_liste_alfabetisk(liste))
