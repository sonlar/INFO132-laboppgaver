'''
Lag en funksjon som tar inn et ord (tekststreng kun bestående av bokstaver)
som argument og returnerer en ny forflyttet tekststreng der hver bokstav
er byttet ut med bokstaven foran i det engelske alfabetet.
For eksempel skal ‘b’ bli ‘a’, ‘c’ bli ‘b’, ‘a’ til ‘z’ osv.
'''


def forflytte_ord(tekst):
    alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    tekst = tekst.lower()
    ny_tekst = ''
    for bokstav in tekst:
        if bokstav in alfabet:
            ny_tekst += alfabet[alfabet.find(bokstav)-1]
    print(ny_tekst)


forflytte_ord('abc')
