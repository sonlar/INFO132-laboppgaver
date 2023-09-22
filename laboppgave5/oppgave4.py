'''
Skriv en funksjon som tar inn en liste med tall
og returnerer gjennomsnittet av tallene. Hvis listen er tom,
skal funksjonen returnere 0.
Formelen for gjennomsnitt er summen av alle tallene delt på lengden av listen.
'''


liste = [2, 4, 6, 8, 10]


def gjennomsnitt(n):
    sum = 0
    for x in range(len(liste)):
        sum += liste[x]
    return sum/len(liste)


print(gjennomsnitt(liste))
