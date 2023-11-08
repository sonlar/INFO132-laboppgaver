"""
telefon.txt der personer er registrert med navn og telefonnummer,
i tilfeldig rekkefølge.
adresse.txt der personer er registrert med navn og adresse.
Denne filen er sortert alfabetisk.

Adresse- og telefonlistene inneholder ikke nødvendigvis de samme personene.

Lag et program som tar utgangspunkt i personene i telefonlisten
og lager en ny fil med kontaktinformasjon for disse.
Alle skal være registrert med telefon samt adresse der den er kjent

Adresselisten er sortert. Utnytt det til å effektivisere
programmet sånn at du unngår unødvendige sammenligninger.
"""


def les_fil(filnavn):
    innhold = ""
    with open(filnavn, "r", encoding="utf-8") as f:
        for linje in f:
            innhold += linje
    return innhold


def flett_fil(filnavn1, filnavn2):
    fil1 = les_fil(filnavn1).split("\n")
    fil2 = les_fil(filnavn2)
    tekst = ""
    for linje in fil1:
        navn = linje[: linje.find(" ")]
        if linje == "":
            continue
        if navn in fil2:
            tekst += f"{linje}{fil2[fil2.find(navn) + len(navn):fil2.find("\n", fil2.find(navn))]}\n"
        else:
            tekst += f"{linje}\n"
    with open("./txt/flettet_fil.txt", "w", encoding="utf-8") as f:
        f.write(tekst)


flett_fil("./txt/telefon.txt", "./txt/adresse.txt")
