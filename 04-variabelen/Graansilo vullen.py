#invoer
b= input('breedte van het veld: ')
l=input( 'lengte van het veld: ')
c= input( 'aantal kubieke meter graan per hectare: ')
h= input( 'hoogte van de silo: ')
r= input( 'straal van de silo: ')

#berekening
pi= 3.14159265359
volume_silo= float(pi)*float(r)*float(r)*float(h)
aantal_silo= volume_silo//float(c)
hoogte_laatste_silo=  volume_silo%float(c)

#uitvoer
print(aantal_silo)
print(hoogte_laatste_silo)
