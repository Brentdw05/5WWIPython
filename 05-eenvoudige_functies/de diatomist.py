#invoer

kleine_r = float(input('wat is de straal van de kleine cirkel: '))

grote_r = float(input('wat is de straal van de grote cirkel: '))

#berekening

n = 0.83*(grote_r**2/kleine_r**2) - 1.9

procent_bedekt  = grote_r/kleine_r*100

#uitvoer

print(str(n), ' kleine cirkels bedekken ', str(procent_bedekt), 'van de grote cirkel' )
