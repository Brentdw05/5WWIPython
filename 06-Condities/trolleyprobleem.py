#invoer

antw_1= str(input('Trek aan de hendel van de wissel: '))
antw_2= str(input('Man van de brug duwen: '))

#berekening
if antw_1 == 'ja' and antw_2 == 'ja':
    doden= 2
elif antw_1 == 'nee' and antw_2 == 'ja':
    doden = 1
elif antw_1 == 'ja' and antw_2 == 'nee':
    doden = 1
else:
    doden = 5
#uitvoer

print(doden)

