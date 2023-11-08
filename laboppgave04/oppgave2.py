def alderstest(alder):
    if alder < 18:
        print(f'Du må vente {18-alder} år til før du kan kjøre bil')
    else:
        print('Du er gammel nok til å kjøre bil')


alderstest(17.9)
