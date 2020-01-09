# invoer

t = int(input('het aantal seconden: '))
aantal_stappen = 0
getal = 0

#berekening

for i in range(0, t):
    t -= 1
    getal += 1
    if getal % 2 == 0:
        aantal_stappen += 1
    else:
        aantal_stappen += 2

#uitvoer

print(aantal_stappen)
