'''
Lag en funksjon som tar inn en tekststreng som argument og
returnerer antall ord i strengen. Test funksjonen med forskjellige strenger.
'''


def antall_ord(tekst):
    ny_tekst = tekst.split()
    print(len(ny_tekst))


tekst = 'hei på deg'
antall_ord(tekst)
