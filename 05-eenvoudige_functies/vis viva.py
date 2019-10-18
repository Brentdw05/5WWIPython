from math import pi

#invoer


r= int(input('de afstand tussen de satelliet en het middelpunt van de aarde: '))

v= int(input('de snelheid van de satelliet ten opzichte van de aarde: '))

#berekening

a= ( pow(r*10, -9) ) / 2 * pow(10, -9) - r*v**2

p= 2 * pi * pow(pow(a, 3)/pow(10, -9), 0.5)

print(a)
print(p)




#uitvoer
