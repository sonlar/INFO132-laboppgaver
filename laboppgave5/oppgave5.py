'''
Skriv en funksjon som lar brukeren angi et tall mellom 1 og 10 som argument.
Funksjonen skal skrive ut et mønster av stjerner "*"
i økende rekkefølge opp til det gitte tallet,
og deretter i synkende rekkefølge tilbake til 1.
Dersom brukeren ikke angir en verdi som argument til funksjonen
skal den skrive ut stjerner opp til tallet 3.
Dersom brukeren setter argumentet til et tall større enn 10
eller mindre enn 1 skal programmet fortsatt skrive ut stjerner opp til tallet 3.
'''


tall = int(input('Vennligst oppgi et tall mellom 1 og 10: '))


def stjerner(tall=3):
    if tall < 1 or tall > 10:
        tall = 3
    for stjerne in range(1, tall+1):
        print('*'*stjerne)
        if stjerne == tall:
            for stjerne in range(tall-1, 0, -1):
                print('*'*stjerne)


stjerner(tall)
