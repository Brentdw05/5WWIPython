#invoer

papierdikte = int(input('geef de dikte van het papier in mm: '))
afstand = int(input('geef de afstand van de aarde tot het hemellichaam in mm: '))
vouwen = 0
papierdikte_eind = 1

#berekening

while afstand != papierdikte and afstand > papierdikte_eind:
    vouwen += 1
    papierdikte_eind = papierdikte_eind * 2


#uitvoer

uitvoer = 'na {} keer vouwen bedraagt de dikte van het papier {} mm.'

print(uitvoer.format(vouwen, papierdikte_eind))
