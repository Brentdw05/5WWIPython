getal = int(input('geef getal: '))

deler = 2

while getal % deler != 0 and getal!= 1:
    deler += 1

if getal == 1:
    print('1 is geen priemgetal')
elif deler != getal:
    print(str(getal)+ ' is geen priemgetal')
else:
    print(str(getal)+ ' is een priemgetal')
