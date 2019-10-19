#invoer

windsnelheid = int(input(' geef een windsnelheid: '))

#berekening

if windsnelheid >= 250:
    uitvoer = 'categorie 5'
elif windsnelheid <= 249 and windsnelheid >= 210:
    uitvoer = 'categorie 4'
elif windsnelheid <= 209 and windsnelheid >= 178:
    uitvoer = 'categorie 3'
elif windsnelheid <= 177 and windsnelheid >= 154:
    uitvoer = 'categorie 2'
elif windsnelheid <= 153 and windsnelheid >= 119:
    uitvoer = 'categorie 1'
else:
    uitvoer = 'geen orkaan'

#uitvoer

print(uitvoer)
