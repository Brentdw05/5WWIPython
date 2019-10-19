#invoer

speler_1 = str(input('de vorm van speler 1: '))

speler_2 = str(input('de vorm van speler 2: '))

#berekening

if speler_1 == speler_2:
    winnaar = 'onbeslist'
elif speler_1 == 'blad' and speler_2 == 'steen':
    winnaar = 'speler 1 wint'
elif speler_1 == 'steen' and speler_2 == 'blad':
    winnaar = 'speler 2 wint'
elif speler_1 == 'steen' and speler_2 == 'schaar':
    winnaar = 'speler 1 wint'
elif speler_1 == 'schaar' and speler_2 == 'steen':
    winnaar = 'speler 2 wint'
elif speler_1 == 'schaar' and speler_2 == 'blad':
    winnaar = 'speler 1 wint'
else:
    winnaar = 'speler 2 wint'

#uitvoer

print(winnaar)
