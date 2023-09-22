import random

antall = random.randint(0, 10)
spørsmåltegn = '?'
antall_spørsmåltegn = print(spørsmåltegn * antall)

print(antall)
gjett = int(input('Gjett hvor mange spørsmålstegn det er ovenfor: '))
print(gjett == antall)
'''
if gjett == antall:
    print('Stemmer')
else:
    print('Feil')
'''
