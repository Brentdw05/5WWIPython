#invoer
a= int(input('getal 1 tussen 0 en 20= '))
b= int(input('getal 2 tussen 0 en 20= '))
#bereking
getal_1= a + b
getal_2= 10*a + 10*b
getal_3= 100*a + 100*b
getal_4= 1000*a + 1000*b
getal_5= 10000*a + 10000*b

#uitvoer
uitvoer= '{:>6} + {:<6} = {:<6}'

print(uitvoer.format(a, b, getal_1))
print(uitvoer.format(10*a, 10*b, getal_2 ))
print(uitvoer.format(100*a, 100*b, getal_3))
print(uitvoer.format(1000*a, 1000*b, getal_4))
print(uitvoer.format(10000*a, 10000*b, getal_5))
