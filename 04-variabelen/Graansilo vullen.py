#invoer
b= float(input('breedte van het veld: '))
l= float(input( 'lengte van het veld: '))
c= float(input( 'aantal kubieke meter graan per hectare: '))
h= float(input( 'hoogte van de silo: '))
r= float(input( 'straal van de silo: '))

#berekening
pi= 3.14159265359
aantal_hectare= (b*l)/10000
volume_silo= pi*r**2*h
totale_opbrengst= c*float(aantal_hectare)
aantal_silo= volume_silo//totale_opbrengst
volume_silo= volume_silo%totale_opbrengst
hoogte_laatste_silo= volume_silo/r**2
aantal_silo += 1

#uitvoer
print(int(aantal_silo))
print(hoogte_laatste_silo)
