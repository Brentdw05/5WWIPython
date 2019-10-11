#42.06826283274985
#13.510020196930185
#kleiner dan of gelijk aan
#'\N{LESS-THAN OR EQUAL TO}'

 #invoer
cijfer_1= input('cijfer 1= ')
cijfer_2= input('cijfer 2= ')
 #berekening
linkerlid = abs(cijfer_1)-abs(cijfer_2)
rechterlid = cijfer_1 - cijfer_2
linkerlid_1 = round(linkerlid, 4)
rechterlid_1 = round(rechterlid, 4)

 #uitvoer
print(str(linkerlid_1) , '\N{LESS-THAN OR EQUAL TO}', str(rechterlid_1))
