'''
Skriv en funksjon som tar et heltall n som argument
og returnerer summen av alle partall fra og med 0 til og med n.
'''


def sum_partall(n):
    partall = 0
    for x in range(n+1):
        if (x % 2 == 0):
            partall += x
    return partall


print(sum_partall(10))
