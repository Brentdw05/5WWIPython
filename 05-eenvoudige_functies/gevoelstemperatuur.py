#invoer

t= input('de luchtemperatuur in °C = ')

w= input('de windsnelheid in km/u = ')

#berekening

gevoelstemperatuur= 13.12 + 0.6215*int(t) + int(0.3965*int(t) - 11.37)*int(pow(3.6*int(w), 0.16))

#uitvoer

print(gevoelstemperatuur)
