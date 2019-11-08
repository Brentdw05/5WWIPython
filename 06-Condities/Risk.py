#invoer

ogen_aanvaller_1= int(input('het aantal ogen van de eerste dobbelsteen van de aanvaller: '))
ogen_aanvaller_2= int(input('het aantal ogen van de tweede dobbelsteen van de aanvaller: '))
ogen_aanvaller_3= int(input('het aantal ogen van de derde dobbelsteen van de aanvaller: '))
ogen_verdediger_1= int(input('het aantal ogen van de eerste dobbelsteen van de verdediger: '))
ogen_verdediger_2= int(input('het aantal ogen van de tweede dobbelsteen van de verdediger: '))

#berekening

verlies_aanvaller = 0
verlies_verdediger = 0

if ogen_aanvaller_1 > ogen_verdediger_1:
    verlies_aanvaller += 0
    verlies_verdediger += 1
elif ogen_aanvaller_1 < ogen_verdediger_1:
    verlies_aanvaller += 1
    verlies_verdediger += 0
elif ogen_aanvaller_2 > ogen_verdediger_2:
    verlies_aanvaller += 0
    verlies_verdediger += 1
elif ogen_aanvaller_2 < ogen_verdediger_2:
    verlies_aanvaller += 1
    verlies_verdediger += 0
else:
    verlies_aanvaller += 2


#uitvoer

print('aanvaller verliest ' + str(verlies_aanvaller)+ ' legers, verdeiger verliest ' + str(verlies_verdediger)+' legers')

#maxi=max(X1 X2 X3 X4)
#mini(X1 X2 X3 X4)
#mid_1=max(min(X1 X2) min(X2 X3) min(X1 X3)
#mid_2=X1+X2+X3+X4-mini-maxi-mid1
#print(maxi,max(mid_1,mid_2),min(mid_1,mid_2),mini)
