#invoer

snelheid_stijn = int(input('Wat is de snelheid van Stijn in m/s: '))
snelheid_kaat = int(input('Wat is de snelheid van Kaat in m/s: '))
afstand = int(input('geef de afstand tussen Stijn en Kaat in m: '))
aantal_seconden = 0

#berekening

while afstand != 0 and afstand > 0:
    afstand -= snelheid_kaat + snelheid_stijn
    aantal_seconden += 1


#uitvoer

uitvoer = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'
print(uitvoer.format(aantal_seconden))
