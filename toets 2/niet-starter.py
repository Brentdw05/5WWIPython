#invoer

getal = float(input('geef een getal tussen 0 en 1: '))
som = 0
aantal_keer_god = 0
n = 0

#berekening

while som < getal:
    n += 1
    som += pow(1 / 2 , n)
    aantal_keer_god += 1


#uitvoer

print(str(aantal_keer_god), str(som))
