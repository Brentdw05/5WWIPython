#invoer
t= input('de luchtemperatuur in °C = ')
w= input('de windsnelheid in km/u = ')

#berekening
gevoelstemperatuur= 13.12 + 0.6215* + (0.3965*t - 11.37)*pow(3.6*w, 0.16)

#uitvoer
print(gevoelstemperatuur)
