# stein-saks-papir
# elif (spiller_valg - datamaskin_valg) == -1 or (spiller_valg - datamaskin_valg) == 2:

import random
spiller_valg = int(input('Velg mellom 1 = stein, 2 = saks, 3 = papir: '))
datamaskin_valg = random.randint(1, 3)

print(f'''Maskinen valgte: {datamaskin_valg}
Jeg vant: {(spiller_valg-datamaskin_valg)%3==2}
Uavgjort: {spiller_valg==datamaskin_valg}
Maskinen vant: {(datamaskin_valg-spiller_valg)%3==2}''')


'''
jeg_vant = False
uavgjort = False
maskinen_vant = False

if spiller_valg == datamaskin_valg:
    uavgjort = True
elif (spiller_valg - datamaskin_valg) % 3 == 2:
    jeg_vant = True
else:
    maskinen_vant = True
'''
