"""
Lag en funksjon som tar inn to tupler og
returnerer en ny tuppel som fletter de to tuplene
(dvs annenhver verdi fra hver av de to argumenttuplene).
Dersom den ene tuppelen er lengre enn den andre,
legges de resterende elementene til slutten.
"""

# finn lengde, for-løkke i range på minste, append begge i hver iterasjon,
# append resten av største etter løkke


def flett_tuppel(tuppel1, tuppel2):
    lengde1, lengde2 = len(tuppel1), len(tuppel2)
    minste = min(lengde1, lengde2)
    ny = list()
    for index in range(minste):
        ny.append(tuppel1[index])
        ny.append(tuppel2[index])
    ny.extend(tuppel1[index + 1 :])
    ny.extend(tuppel2[index + 1 :])
    return tuple(ny)


print(flett_tuppel((1, 2, 3), (4, 5, 6)))
