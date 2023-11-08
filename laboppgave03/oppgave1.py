alder = int(input('Angi din alder: '))


def magiskdrikke(alder):
    if alder < 20:
        alder += 10
    elif alder >= 20:
        alder -= 5
    return alder


print(magiskdrikke(alder))
