
som = 0
prijs = 1

while prijs != 0:
    prijs = float(input('geef prijs: '))
    som += prijs

som = round(som,2)

print('De totale prijs is € ' + str(som))
