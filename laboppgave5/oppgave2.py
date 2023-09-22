'''
Skriv en funksjon kalt "delbar_3" som tar et heltall n som argument.
Funksjonen skal skrive ut alle tall fra og med 1 til og med n på hver sin linje.
Hvis tallet er delelig med 3 skal du skrive ut "delbar på 3" på en ny linje.
'''


def delbar_3(n):
    for x in range(1, n+1):
        print(x)
        if (x % 3 == 0):
            print('delbar på 3')


delbar_3(10)
