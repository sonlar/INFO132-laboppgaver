antall_studenter = 55
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter
# print('kvinneandelen er ', kvinneandel)
print(f'kvinneandelen er {kvinneandel:.2f}')

"""

Oppgave 2 (middels).

2a)  Finn feilen i de følgende programmene og bestem om det er snakk om en syntaktisk, logisk eller semantisk feil, jfr avsnitt 1.10 i læreboken. (Kjør gjerne programmene i IDLE for å se hvilke feilmeldinger som gis.)

 

i)

antall_studenter = 55
antall_kvinner = 32
kvinneandel = Antall_kvinner/antall_studenter # syntaks, stor a i Antall_kvinner når variabel bruker liten a
print('kvinneandelen er ', kvinneandel)

 

ii)

antall_studenter = 55
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter 
print(kvinneandelen er , kvinneandel) # syntaks, mangler "" rundt string/tekst delen (kvinneandelen er)

 

iii)

antall_studenter = 55 
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter 
print('kvinneandelen er ' kvinneandel) # syntaks, mangler , før variabel

 

iv)

kvinneandel = antall_kvinner/antall_studenter #logisk, bruker variabler før de har blitt gitt en verdi
antall_studenter = 55
antall_kvinner = 32
print('kvinneandelen er ', kvinneandel)

 

v)

kvinneandel = antall_kvinner=32/antall_studenter=55 # logisk/semantisk? gir variabel verdi i samme linje du bruker dem
print('kvinneandelen er ', kvinneandel)

 

vi)

antall_studenter = 55
antall_kvinner = 32
kvinneandel = antall_studenter/antall_kvinner #logisk/semantisk? feil rekkefølge på variabler
print('kvinneandelen er ', kvinneandel)

"""
