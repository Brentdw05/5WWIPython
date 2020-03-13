from math import sin, cos, pi

#invoer

getal = str(input('geef een getal: '))
x_coordinaat, y_coordinaat = 0, 0
hoek = pi / 5

#berekening

for c in getal:
    if c == '.':
        pass
    else:
        x_coordinaat += sin(int(c) * hoek)
        y_coordinaat += cos(int(c)* hoek)
#uitvoer

uitvoer = 'Getal {} wandelt naar positie ({:.2f}, {:.2f}).'

print(uitvoer.format(getal, x_coordinaat, y_coordinaat))
