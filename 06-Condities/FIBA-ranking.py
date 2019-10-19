#invoer

doelpunten_thuisploeg = int(input('geef het aantal doelpunten van de thuisploeg : '))

doelpunten_uitploeg = int(input('geef het aantal doelpunten van de uitploeg : '))

#berekening

doelpunten_verschil = abs(doelpunten_thuisploeg - doelpunten_uitploeg)

if doelpunten_thuisploeg > doelpunten_uitploeg:
    if doelpunten_verschil < 10:
        punten_thuisploeg = 530
        punten_uitploeg= 470
    elif doelpunten_verschil >= 10 and doelpunten_verschil < 20:
        punten_thuisploeg = 630
        punten_uitploeg = 370
    else:
        punten_thuisploeg = 730
        punten_uitploeg= 270
else:
    if doelpunten_verschil < 10:
        punten_uitploeg = 670
        punten_thuisploeg= 330
    elif doelpunten_verschil >= 10 and doelpunten_verschil < 20:
        punten_uitploeg = 770
        punten_thuisploeg = 230
    else:
        punten_uitploeg = 870
        punten_thuisploeg= 130



#uitvoer

uitvoer = '{:>12} {:.2f} '

print(uitvoer.format('thuisploeg:',punten_thuisploeg))
print(uitvoer.format('uitploeg:', punten_uitploeg))
