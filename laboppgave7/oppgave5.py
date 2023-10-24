'''Lag en funksjon som tar inn en liste av tekststrenger som argument.
Funksjonen skal returnere en ny liste der alle tekststrengene er reversert.'''


def baklengs_liste(liste):
    baklengs = []
    for item in liste:
        baklengs_item = item[::-1]
        baklengs.append(baklengs_item)
    print(baklengs)


liste = ['hello', 'world', 'Spam', 'Egg']
baklengs_liste(liste)
