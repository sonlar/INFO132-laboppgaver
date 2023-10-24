'''
Lag en funksjon som tar inn en tekststreng og
sjekker hvor mange ganger hvert tegn forekommer i strengen.
Funksjonen skal skrive ut på en ny linje for hvert tegn i strengen
antallet ganger tegnet forekommer. Test funksjonen med forskjellige strenger.
'''


def antall_tegn(tekst):
    ny_tekst = ''
    for bokstav in tekst:
        if bokstav not in ny_tekst:
            ny_tekst += f'"{bokstav}": {tekst.count(bokstav)} '
    print(ny_tekst)


tekst = 'du ringer vi bringer'
antall_tegn(tekst)
