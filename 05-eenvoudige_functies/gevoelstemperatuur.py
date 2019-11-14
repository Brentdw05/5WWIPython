#invoer

t= float(input('de luchtemperatuur in °C = '))

w= float(input('de windsnelheid in km/u = '))

#berekening

w = w/3.6
gevoelstemperatuur= 13.12 + 0.6215*t + (0.3965*(t) - 11.37)*(pow(3.6*w, 0.16))

#uitvoer

print(gevoelstemperatuur)
