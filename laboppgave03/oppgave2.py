'''
Hvis inntekten er over 500 000, er skatteprosenten 30%.
Hvis inntekten er 500 000 eller mindre, er skatteprosenten 20%.
Programmet informerer brukeren om hvor mye skatt som skal betales
'''

inntekt = int((input('Hva er din inntekt?: ')))


def skatt(inntekt):
    if inntekt > 5e5:
        inntekt *= 0.3
    elif inntekt <= 5e5:
        inntekt *= 0.2
    print(f'Du skal betale {inntekt} kroner i skatt')


skatt(inntekt)
