
#kleiner dan of gelijk aan
#'\N{LESS-THAN OR EQUAL TO}'

 #invoer
cijfer_1= float(input('cijfer 1= '))
cijfer_2= float(input('cijfer 2= '))
 #berekening
linkerlid = abs(cijfer_1-cijfer_2)
rechterlid = abs(abs(cijfer_1) - abs(cijfer_2))
linkerlid = round(linkerlid, 4)
rechterlid = round(rechterlid, 4)

 #uitvoer
print(str(rechterlid) , '\N{LESS-THAN OR EQUAL TO}', str(linkerlid))
