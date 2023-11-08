'''
hundrerplass = tall // 100
tierplass = tall // 10 % 10
enerplass = tall % 10
'''
tall = int(input('Vennligst oppgi et tresifret tall under: \n'))
tallet = [tall // 100, tall // 10 % 10, tall % 10]
rekkefølge = []
'''
x = 0
while x < 2:
    rekkefølge.append(f'{tallet[0]}{tallet[1+x]}{tallet[2-x]}')
    x += 1

x = 0
while x < 2:
    rekkefølge.append(f'{tallet[1]}{tallet[0-x]}{tallet[2-2*x]}')
    x += 1

x = 0
while x < 2:
    rekkefølge.append(f'{tallet[2]}{tallet[0+x]}{tallet[1-x]}')
    x += 1

'''
x = 0
print()
for i in range(2):
    rekkefølge.append(f'{tallet[0]}{tallet[1+x]}{tallet[2-x]}')
    rekkefølge.append(f'{tallet[1]}{tallet[0-x]}{tallet[2-2*x]}')
    rekkefølge.append(f'{tallet[2]}{tallet[0+x]}{tallet[1-x]}')
    x += 1

rekkefølge.sort()
print(' '.join(rekkefølge))
