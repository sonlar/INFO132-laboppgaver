alder = int(input('Hva er din alder?: '))


def stemmerett(alder):
    if alder < 18:
        print('Du er for ung til å stemme!')
    else:
        stemt = input('Har du allerede stemt? (ja/nei): ')
        if stemt == 'ja':
            print('Da kan du ikke stemme igjen!')
        if stemt == 'nei':
            parti = input('Hvilket parti vil du stemme på? ')
            print(f'Du har stemt på {parti}.')


stemmerett(alder)
