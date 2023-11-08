forbruk = int(input('Hva er ditt strømforbruk i kWh?: '))


def strømforbruk(forbruk):
    if forbruk < 200:
        print('Bra jobbet! Du bruker lite strøm!')
    elif forbruk >= 200 and forbruk <= 500:
        svar = input('Bruker du energisparende apparater? (ja/nei): ')
        if svar == 'nei':
            print('Det er ingen bedre tid enn nå å starte!')
        if svar == 'ja':
            print('Bra jobbet! Du bruker lite strøm!')
    if forbruk > 500:
        print('Ditt forbruk er høyt! Du burde vurdere å gjøre tiltak for å kutte ned på forbruk')


strømforbruk(forbruk)
