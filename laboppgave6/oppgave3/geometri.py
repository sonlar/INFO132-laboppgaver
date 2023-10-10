'''
Lag en Python-fil som heter geometri.py som inneholder funksjoner
for å beregne området av en firkant og en sirkel.
'''
from math import pi


def areal_firkant(bredde, lengde):
    return bredde*lengde


def areal_sirkel(radius):
    return f'{pi*radius**2:.2f}'
