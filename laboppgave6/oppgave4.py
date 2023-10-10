'''
 Lag en Python-klasse kalt Person som har følgende attributter:

    navn
    alder

Person-klassen skal ikke ha noen metoder.
'''


class Person:
    navn = None
    alder = None

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder


'''
Lag en Python-klasse kalt Bil som har følgende attributter:

    merke
    modell
    eier (et objekt fra Person-klassen fra 4a)

Skriv også en metode i Bil-klassen som kan skrive ut eieren av bilen.
'''


class Bil:

    def __init__(self, merke, modell, eier):
        self.merke = merke
        self.modell = modell
        self.eier = Person.navn

    def utskrift_eier(self):
        print(f'Eieren av {self.merke} {self.modell} er {self.eier}')


person1 = Person('Kari', 40)
person2 = Person('Knut', 30)
person1_bil = Bil('Volvo', 1, person1)
person2_bil = Bil('Fiat', 400, person2)
person1_bil.eier = person1.navn


person1_bil.utskrift_eier()
