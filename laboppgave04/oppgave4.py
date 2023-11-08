
def tidsjekk(tid, plural="er"):
    '''Sjekker om tidsenhetene skal returneres i entall eller flertall form'''
    if tid == 1:
        return ''
    else:
        if plural == 'er':
            return 'er'
        else:
            return 'r'


def tidkonvertering(tid):
    '''konverterer tid som er gitt i sekunder til formatet:
     x time(r), y minutt(er), z sekund(er)'''
    time = 0
    minutt = 0
    sekund = 0
    while tid > 0:
        if tid >= 3600:
            time += 1
            tid -= 3600
        elif tid >= 60:
            minutt += 1
            tid -= 60
        elif tid > 0:
            sekund += 1
            tid -= 1
    return (
        f'{time} time{tidsjekk(time,"r")}, '
        f'{minutt} minutt{tidsjekk(minutt)}, '
        f'{sekund} sekund{tidsjekk(sekund)}')


print(tidkonvertering(3721))
