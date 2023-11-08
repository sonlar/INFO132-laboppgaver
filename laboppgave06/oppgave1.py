'''
Lag en liste med navnene på dine fem favorittfrukter.
Skriv deretter kode for følgende operasjoner:
    1. Skriv ut hele listen med favorittfrukter.
    2. Legg til en ny frukt i listen.
    3. Fjern den andre frukten i listen.
    4. Finn lengden (antall elementer) i listen.
    5. Sjekk om "banan" er i listen.
'''

frukt = ['Eple', 'Banan', 'Appelsin', 'Kiwi', 'Mango']
frukt += ['Pære']
frukt.pop(1)
antall = len(frukt)
print('Banan' in frukt)
print(frukt)
