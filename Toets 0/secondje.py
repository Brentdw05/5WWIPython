#invoer
s= int(input('aantal seconden: '))

#berekening
aantal_dagen= s//86400
s= s%86400

aantal_uren= s//3600
s= s%3600

aantal_minuten= s//60

aantal_seconden= s%60



#uitvoer
print(str(aantal_dagen)+ 'd '+str(aantal_uren)+':'+str(aantal_minuten)+':'+str(aantal_seconden))
