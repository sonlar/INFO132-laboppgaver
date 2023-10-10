'''
Utvid Python-klassen kalt Student som har følgende attributter:

    navn
    alder
    studieretning

Legg til følgende metoder i klassen:

    def skriv_navn(self): En metode som skriver ut studentens
    navn med følgende setning: "Studenten heter {navn}".
    def returner_alder(self): En metode som returnerer studentens alder.
    def skriv_studieretning(self): En metode som skriver ut studentens
    studieretning med følgende setning: "{navn} studerer {retning}".
'''


class Student:
    def __init__(self, navn, alder, studieretning):
        self.navn = navn
        self.alder = alder
        self.studieretning = studieretning

    def skriv_navn(self):
        print(f'Studenten heter {self.navn}')

    def returner_alder(self):
        return self.alder

    def skriv_studieretning(self):
        print(f'{self.navn} studerer {self.studieretning}')


student1 = Student('Kari', 21, 'INFOVIT')

student1.skriv_navn()
print(student1.returner_alder())
student1.skriv_studieretning()
