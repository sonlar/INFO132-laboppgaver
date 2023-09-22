'''
Lag en funksjon som tar en setning og et tegn som argument.
Funksjonen skal telle hvor mange ganger det gitte tegnet
opptrer i setningen og skrive ut dette antallet.
Hvis tegnet ikke finnes i setningen,
skal den skrive ut 'Tegnet "[tegn]" ble ikke funnet.'
'''


def telle_tegn(setning, tegn):
    teller = 0
    if tegn in setning:
        for x in range(len(setning)):
            if (tegn == setning[x]):
                teller += 1
        print(f'Tegnet "{tegn}" ble funnet {teller} ganger.')
    else:
        print(f'Tegnet "{tegn}" ble ikke funnet.')


def telle_tegn2(setning, tegn):
    teller = 0
    leter = setning.find(tegn)
    if tegn in setning:
        while leter != -1:
            teller += 1
            setning = setning[leter+1:]
            leter = setning.find(tegn)
        print(f'Tegnet "{tegn}" ble funnet {teller} ganger.')
    else:
        print(f'Tegnet "{tegn}" ble ikke funnet.')


telle_tegn('dette er en setning', 'e')
telle_tegn2('dette er en setning', 'e')
