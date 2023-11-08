"""
Lag et GUI-program som simulerer en avstemning.
Programmet skal ha en knapp for hvert alternativ,
og en «Resultat»-etikett ("label") som viser
hvor mange stemmer hvert alternativ har.
Programmet skal lagre antall stemmer for hvert alternativ i en liste.
"""

from tkinter import Button, Label, Tk

ordbok = dict()


def klikk(alternativ):
    ordbok[alternativ] = ordbok.get(alternativ, 0) + 1
    resultat.config(text=ordbok)


window = Tk()
knapp1 = Button(window, text="Alternativ 1", command=lambda: klikk("Alternativ 1"))
knapp2 = Button(window, text="Alternativ 2", command=lambda: klikk("Alternativ 2"))
knapp3 = Button(window, text="Alternativ 3", command=lambda: klikk("Alternativ 3"))
knapp1.pack()
knapp2.pack()
knapp3.pack()
resultat = Label(window, text="")
resultat.pack()
window.mainloop()
