#invoer

aantal_elektronen = int(input('het aantal elektronen: '))

#berekening

if aantal_elektronen > 2 and aantal_elektronen < 10:
    schil = 'L'
elif aantal_elektronen >= 10 and aantal_elektronen < 28:
    schil  = 'M'
elif aantal_elektronen >= 28 and aantal_elektronen < 60:
    schil  = 'N'
elif aantal_elektronen >= 60 and aantal_elektronen < 92:
    schil  = 'O'
elif aantal_elektronen >= 92 and aantal_elektronen <= 124:
    schil = 'P'
elif aantal_elektronen > 124 and aantal_elektronen <= 156:
    schil  = 'Q'
else:
    schil = 'K'


#uitvoer

print('De ' + str(schil) + '-schil is de buitenste schil van een stabiel atoom met ' + str(aantal_elektronen) + ' elektronen.')
