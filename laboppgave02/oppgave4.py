import math
siffer1 = str(5)
siffer2 = str(10)
kombo1 = siffer1 + siffer2
kombo2 = siffer2 + siffer1
utregning = math.sqrt(int(kombo1) * int(kombo2))

print(f'Kvadratroten av {kombo1} * {kombo2} = {utregning}')
