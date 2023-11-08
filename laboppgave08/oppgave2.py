"""
Lag en funksjon som tar inn navnet på en fil og en bokstav,
og returnerer alle ordene i filen som begynner med den spesifikke bokstaven.
Funksjonen skal returnere ordene som en liste.
Test funksjonen med forskjellige filer og bokstaver.
"""


def filtrer_ord(fil, bokstav):
    liste = []
    with open(fil, "r") as f:
        for linje in f:
            for ord in linje.split():
                if ord[0].lower() == bokstav:
                    liste.append(ord)
        return liste


print(filtrer_ord("./txt/lorem.txt", "d"))
