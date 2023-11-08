"""
Skriv en funksjon som tar inn en fortegnelse av navn og deres tilsvarende alder,
og returnerer en ny liste med navnene på personene som er over en viss alder.
Alderen som skal sjekkes mot, skal også være en parameter for funksjonen.
"""


def navn_over_alder(dict, aldersgrense):
    ny_liste = list()
    for key in dict:
        if dict[key] < aldersgrense:
            continue
        ny_liste.append(key)
    return ny_liste


dict = {"Jens": 20, "Alf": 40, "Hanne": 35, "Mona": 30}
print(navn_over_alder(dict, 31))
