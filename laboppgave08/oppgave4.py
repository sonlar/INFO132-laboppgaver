"""
Lag et program som leser inn ordlisten,
lar brukeren taste inn norske søkeord og
svarer med den engelske oversettelsen hvis den finnes.
Finn alle oppslag i ordlisten som begynner med brukerens søkeord.
"""


def ordliste(filnavn):
    print(f"Oppgi søkeord (avslutt med {"slutt"})")
    counter = 0
    with open(filnavn, "r", encoding="utf-8") as f:
        while True:
            søk = input("Søkeord: ")
            if søk == "slutt":
                break
            for linje in f:
                if søk in linje:
                    counter += 1
                    pos = linje.find(søk)
                    poskomma = linje.find(",", pos)
                    print(
                        f"{linje[pos:poskomma]} = {linje[poskomma + 1:].strip()}"
                    )
            if counter == 0:
                print(f"{søk} finnes ikke i ordlisten.")


ordliste("./txt/ordliste.txt")
