from random import randint

munt = 0
aantal_experimenten = 1000000

for i in range(aantal_experimenten):
    munt += randint(0,1)

print('munt:',munt / aantal_experimenten,'kop:',(aantal_experimenten - munt)/aantal_experimenten)
