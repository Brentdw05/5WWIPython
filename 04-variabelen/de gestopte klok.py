#invoer
a= input('het uur waarop ze vertrekt: ')
b= input('het aantal minuten waarop ze vertrekt: ')
c= input('het uur waarop ze aankomt bij haar vriendin: ')
d= input('het aantal minuten waarop ze aankomt bij haar vriendin: ')
e= input('het uur waarop ze vertrekt naar huis: ')
f= input('het aantal minuten waarop ze vertrekt naar huis: ')
g= input('het uur waarop ze terug thuiskomt: ')
h= input('het aantal minuten waarop ze terug thuis aankomt: ')

#berekening
i= a*60
j= c*60
k= e*60
l= g*60
m= i+b+j+d+k+f+l+h
n= j+d+k+f
o= int((int(m)-int(n))//2)



print(o)
#uitvoer
print()

