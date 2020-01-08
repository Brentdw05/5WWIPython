# invoer

t = input('het aantal seconden: ')
aantal_stappen = 0

#berekening

for i in (0, t):
    getal = i
    if getal % 2 == 0:
        aantal_stappen += 1
    else:
        aantal_stappen += 2


#uitvoer

print(aantal_stappen)
