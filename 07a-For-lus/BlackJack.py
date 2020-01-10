#invoer

waarde = int(input('geef een kaartwaarde: '))
invoer = waarde
#berekening

while waarde < 21 and invoer != 0 :
    invoer = int(input('geef een kaartwaarde: '))
    waarde += invoer

if waarde > 21:
    uitvoer = 'Verbrand ({})'
elif waarde < 21:
    uitvoer = 'Voorzichtig gespeeld ({})'
else:
    uitvoer = 'Gewonnen!'

#uitvoer

print(uitvoer.format(waarde))
