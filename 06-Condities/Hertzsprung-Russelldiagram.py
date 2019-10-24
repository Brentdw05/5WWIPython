#invoer

temperatuur= float(input('temperatuur van de ster: '))
lichtsterkte= float(input('lichtsterkte van de ster: '))

#berekening

if temperatuur > 3000 and lichtsterkte <= 0.01:
    soort = 'kleine dwergen'
elif lichtsterkte > 0.01 and lichtsterkte < 10:
    soort = 'hoofdreeks'
elif temperatuur <= 6000 and lichtsterkte > 10 and lichtsterkte < 100
    soort = 'reuzen'
elif lichtsterkte >= 100 and lichtsterkte < 1000:
    soort = 'heldere reuzen'
elif lichtsterkte >= 1000 and lichtsterkte < 10000:
    soort = 'superreuzen (b)'
else:
    soort = 'superreuzen (a)'

#uitvoer

print(soort)
