#invoer
N_60 = int(input('geef de aantal tjirps per minuut: '))

#berekening
T_f= 50 + ((N_60-40)/4)
T_c= 10 +((N_60-40)/7)
#uitvoer
print('temperatuur (Fahrenheit):', T_f)
print('temperatuur (Celsius):', T_c)
