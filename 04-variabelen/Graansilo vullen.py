#invoer
b= input('breedte van het veld: ')
l=input( 'lengte van het veld: ')
c= input( 'aantal kubieke meter graan per hectare: ')
h= input( 'hoogte van de silo: ')
r= input( 'straal van de silo: ')

#berekening
pi= 3.14159265359
aantal_hectare= (float(b)*float(l))/10000
volume_silo= float(pi)*float(r)*float(r)*float(h)
totale_opbrengst= float(c)*float(aantal_hectare)
aantal_silo= volume_silo//totale_opbrengst
hoogte_laatste_silo=  volume_silo%totale_opbrengst

#uitvoer
print(aantal_silo+1)
print(hoogte_laatste_silo)
