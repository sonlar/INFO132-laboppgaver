'''
Lag en funksjon som tar inn en tekststreng og
sjekker om den er et palindrom.
En palindromstreng er en streng som kan leses likt både baklengs og framover.
Funksjonen skal returnere True hvis strengen er et palindrom og False ellers.
Test funksjonen med forskjellige strenger.
'''


def palindrom_sjekk(tekst):
    baklengs = tekst[::-1]
    print(tekst == baklengs)


tekst1 = 'tacocat'
tekst2 = 'taco cat'

palindrom_sjekk(tekst1)
palindrom_sjekk(tekst2)
