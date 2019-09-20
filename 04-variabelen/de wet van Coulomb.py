# invoer
r= float(input('r= '))
r= r*10E-2
k_0= 8.99*10**9
q_1 = 2.0 * 10E-6
q_2 = 1.0 * 10E-6
# berekening
f_c= k_0*q_1*q_2/r**2

# uitvoer
print(f_c)
