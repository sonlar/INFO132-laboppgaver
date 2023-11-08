# celsius til fahrenheit F=(C*9/5)+32
# fahrenheit til celsius C=(F-32)*5/9

celsius = 15.56
fahrenheit = 60

celsius_formel = (celsius*9/5)+32
fahrenheit_formel = (fahrenheit-32)*5/9

celsius_setning = (
    f'{celsius:.2f}\N{degree celsius}  '
    f'= {celsius_formel:.2f}\N{degree fahrenheit}'
)
fahrenheit_setning = (
    f'{fahrenheit:.2f}\N{degree fahrenheit}  '
    f'= {fahrenheit_formel:.2f}\N{degree celsius}'
)
print(celsius_setning)
print(fahrenheit_setning)

'''
Noen ganger så viser ikke programmet helt indentiske tall mellom
fahrenheit og celsius selvom de skal være identiske.
Det har med at når det blir for mange desimaler så blir de rundet av

'''
