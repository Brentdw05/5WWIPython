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
