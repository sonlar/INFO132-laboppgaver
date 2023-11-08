"""
Lag et GUI-program som har et tekstfelt og en knapp.
Når brukeren skriver inn tekst i tekstfeltet og trykker på knappen,
skal programmet vise teksten i et etikettfelt.
"""

from tkinter import Button, Entry, Label, Tk

window = Tk()
tekstfelt = Entry(window)
tekstfelt.pack()


def klikk():
    tekst.config(text=tekstfelt.get())


knapp = Button(window, text="vis tekst", command=klikk)
knapp.pack()
tekst = Label(window, text="")
tekst.pack()
window.mainloop()
