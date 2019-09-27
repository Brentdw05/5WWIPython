#invoer
i_l= input('de kans op leven op een planeet rond een ster in onze melkweg: ')
f_i= input('fractie van die planeten, waar zich intelligent leven ontwikkelt: ')
L= input('gemiddelde levensduur van communicerende beschavingen in jaren: ')

#berekening
R=2
f_c=0.2
N= R*f_c*float(i_l)*float(f_i)*float(L)

#uitvoer

print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren: '+ str(int(N)))
