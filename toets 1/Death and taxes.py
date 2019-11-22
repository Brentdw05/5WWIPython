#invoer

bruto_jaarsalaris = float((input('wat is het jaarsalaris: ')))

#berekening

rsz = bruto_jaarsalaris / 100 * 13.07

netto_jaarsalaris = bruto_jaarsalaris - rsz

netto_jaarsalaris_schijf1 = netto_jaarsalaris - 13250

netto_jaarsalaris_schijf2 = netto_jaarsalaris_schijf1 - 10140

netto_jaarsalaris_schijf3 = netto_jaarsalaris_schijf2 - 17090

voorheffing = 0

if netto_jaarsalaris <= 13250:
    voorheffing += netto_jaarsalaris / 100 * 25
elif netto_jaarsalaris_schijf1 <= 10140:
    voorheffing += netto_jaarsalaris_schijf1 / 100 * 40
elif netto_jaarsalaris_schijf2 <= 17090:
    voorheffing += netto_jaarsalaris_schijf2 / 100 * 45
else:
    voorheffing += netto_jaarsalaris_schijf3 / 100 * 50



netto_jaarsalaris_einde = bruto_jaarsalaris - rsz - voorheffing

netto_maandsalaris = netto_jaarsalaris_einde / 12

#uitvoer

uitvoer = '{:<20.2f}'

print('+ brutojaarsalaris ' + uitvoer.format(bruto_jaarsalaris))
print('- rsz '+ uitvoer.format(rsz))
print('- voorheffing ' + uitvoer.format(voorheffing))
print('==============================')
print('+ netto jaarsalaris ' + uitvoer.format(netto_jaarsalaris_einde))
print('+ netto maandsalaris ' + uitvoer.format(netto_maandsalaris))
