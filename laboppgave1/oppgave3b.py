# celsius til fahrenheit F=(C*9/5)+32

try:
    celsius = float(input('Skriv inn Celsius grader: '))
    celsius_formel = print((celsius * 9 / 5) + 32)
except ValueError:
    print('Vennligst skriv inn et tall')
