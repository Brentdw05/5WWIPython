#invoer
t= int(input('tijd(in nanoseconden): ' ))

#berekening
n=1.000277
c=299792458
d=(c*t*10**-9)/(2*n)

#uitvoer
print(d,' meter')
