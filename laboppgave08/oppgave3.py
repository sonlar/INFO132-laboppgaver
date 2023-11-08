"""
Lag en funksjon som tar inn navnet på en fil, et gammelt ord, og et nytt ord,
og erstatter alle forekomster av det gamle ordet med det nye ordet i filen.
Funksjonen trenger ikke returnere noen verdi,
men filen skal være endret etter funksjonskallet.
Test funksjonen med forskjellige filer og ord.
"""


def les_fil(fil):
    text = ""
    with open(fil, "r", encoding="utf-8") as f:
        for linje in f:
            text += linje
    return text


def erstatt_ord(fil, gammelt_ord, nytt_ord):
    tekst = les_fil(fil).replace(gammelt_ord, nytt_ord)
    with open(fil, "w", encoding="utf-8") as f:
        f.write(tekst)


erstatt_ord("./txt/hund.txt", "hund", "katt")
