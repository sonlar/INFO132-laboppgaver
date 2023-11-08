"""
Lag en funksjon som tar inn navnet på en fil og teller antall linjer i filen.
Funksjonen skal returnere antall linjer som et heltall.
Test funksjonen med forskjellige filer.
"""


def antall_linjer(fil):
    with open(fil, "r") as f:
        counter = 0
        for linje in f:
            counter += 1
        return counter


print(antall_linjer("./txt/lorem.txt"))
