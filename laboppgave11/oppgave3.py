"""
Lag et GUI-program som har tre skyvespaker ("scales" eller "sliders")
- en for hver av de tre RGB-fargekomponentene.
Når brukeren justerer en spake, skal bakgrunnsfargen
til et etikettfelt endres i henhold til de valgte RGB-verdiene.
"""
from tkinter import Label, Scale, Tk


def oppdater_farge(fargekode):
    R = slider1.get()
    G = slider2.get()
    B = slider3.get()
    RGB = f"#{R:02x}{G:02x}{B:02x}"
    farge_label.config(bg=RGB)


window = Tk()

label1 = Label(window, text="Rød")
label2 = Label(window, text="Grønn")
label3 = Label(window, text="Blå")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

slider1 = Scale(window, from_=0, to=255, command=oppdater_farge)
slider2 = Scale(window, from_=0, to=255, command=oppdater_farge)
slider3 = Scale(window, from_=0, to=255, command=oppdater_farge)
slider1.grid(row=1, column=0)
slider2.grid(row=1, column=1)
slider3.grid(row=1, column=2)

farge_label = Label(window, height=10, width=40, bg="#000000")
farge_label.grid(row=2, column=1)
window.mainloop()
