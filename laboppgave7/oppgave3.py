'''
Lag en funksjon som tar inn en liste av tekststrenger
som argument og returnerer en ny liste med de tekststrengene
som har en lengde på minst 5 tegn. Test funksjonen med forskjellige lister.
'''


def større_enn_fem(liste):
    ny_liste = []
    for item in liste:
        if len(item) >= 5:
            ny_liste.append(item)
    print(ny_liste)


liste = ['eple', 'banan', 'pære', 'drue', 'ananas']
større_enn_fem(liste)


'''
Lag en funksjon som heter større_enn_n som tar inn en liste og
et tall n som argumenter.
Returner en ny liste med alle tekststrengene som har en lengde på større enn n.
'''


def større_enn_n(liste, tall):
    ny_liste = []
    for item in liste:
        if len(item) >= tall:
            ny_liste.append(item)
    print(ny_liste)


større_enn_n(liste, 4)
