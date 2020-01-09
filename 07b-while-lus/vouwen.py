#invoer

papierdikte = int(input('geef de dikte van het papier in mm: '))
afstand = int(input('geef de afstand van de aarde tot het hemellichaam in mm: '))
vouwen = 1
papierdikte_eind = 0

#berekening

while afstand != papierdikte:
    vouwen += 1
    papierdikte_eind += papierdikte * 2


#uitvoer

uitvoer = 'na {:.f} keer vouwen bedraagt de dikte van het papier {:.f} mm.'

print(uitvoer.format(vouwen, papierdikte_eind))
