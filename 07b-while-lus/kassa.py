
som = 0
prijs = 1

while prijs != 0:
    prijs = float(input('geef prijs: '))
    som += prijs

som = round(som , 2)

uitvoer = 'De totale prijs is € {:.2f}'

print(uitvoer.format(som))
