'''
Lag en funksjon som tar inn to tekststrenger som argumenter og
sjekker om den første strengen er en del av den andre strengen.
Funksjonen skal returnere True hvis den første strengen finnes
i den andre strengen, og False ellers.
Test funksjonen med forskjellige strenger.
'''


def sammenlign_tekst(itekst, tekst):
    print(itekst in tekst)


itekst = 'som'
tekst = 'hva som helst'
sammenlign_tekst(itekst, tekst)
