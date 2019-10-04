from math import sqrt
#92.06826
#16.1


a = float(input('lengte zijde a: '))
b = float(input('lengte zijde b: '))
c = sqrt(pow(a, 2) + pow(b, 2))

uitvoer = 'In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'

print(uitvoer.format(a, b, c))
