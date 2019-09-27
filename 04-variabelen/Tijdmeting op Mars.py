#invoer
sol=int(input('aantal marsdagen: '))

#berekening
sol_1= 3600*24+39*60+35.244
sol_s= sol*sol_1

aantal_dagen= int(sol_s//86400)
sol_s= sol_s%86400

aantal_uren= int(sol_s//3600)
sol_s= sol_s%3600

aantal_minuten=int(sol_s//60)
aantal_seconden= int(sol_s%60)


#uitvoer
print(str(sol)+' sol = '+ str(aantal_dagen)+' dagen, '+str(aantal_uren)+' uren, '+str(aantal_minuten)+' minuten en '+str(aantal_seconden)+' seconden')
