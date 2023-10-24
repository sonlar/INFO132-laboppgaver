"""
Vi ser videre på en sortert adresseliste som også heter adresse.txt.
Lag en funksjon sett_inn(person, fil)
som kan sette inn en ny person/adresse på riktig sted i filen,
sånn at den forblir sortert.

Funksjonen skal være generell nok til å behandle alle slags tekster på formen
bokstaver-mellomrom-tegn, for eksempel ’Kari 98654321’ .

 Bruk funksjonen sett_inn() til å lage en ny funksjon som kan skrive
en sortert versjon av telefon.txt i en ny fil sortert_telefon.txt.
"""


import os


def sett_inn(filnavn, adresse):
    tekst = ""
    adresse_navn = adresse[: adresse.find(" ")]
    adresse_sannhet = True

    with open(filnavn, "r", encoding="utf-8") as f:
        for linje in f:
            linje_navn = linje[: linje.find(" ")]
            if adresse_sannhet is True and adresse_navn < linje_navn:
                tekst += adresse + "\n"
                adresse_sannhet = False
            tekst += linje
        if adresse not in tekst:
            tekst += adresse + "\n"

    filkatalog, filnavn = os.path.split(filnavn)
    ny_filnavn = os.path.join(filkatalog, "ny-" + filnavn)
    with open(ny_filnavn, "w", encoding="utf-8") as f:
        f.write(tekst)


sett_inn("./txt/adresse.txt", "Åge rettvei 1")
sett_inn("./txt/telefon.txt", "Åge 12300321")
