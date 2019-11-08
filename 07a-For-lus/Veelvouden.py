#invoer

getal = int(input("geef een getal: "))
som = 0

#berekening

for veelvoud in range(getal, 101, getal):
    som += veelvoud

#uitvoer

print(som)
