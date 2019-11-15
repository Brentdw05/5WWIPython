#invoer

dag = int(input('wat is de dag: '))
maand = int(input('wat is de maand: '))
jaar = int(input('wat is het jaar: '))

#berekening

jaar_4 = jaar % 4
jaar_100 = jaar % 100
jaar_400 = jaar % 400

if dag == 31 and maand == 12:
    dag = 1
    maand = 1
    jaar += 1
elif dag == 31:
    if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10 or maand == 12:
        dag = 1
        maand += 1
elif dag == 30:
    if maand == 4 or maand == 6 or maand == 9 or maand == 11:
        dag = 1
        maand += 1
elif dag == 28 and maand == 2 and jaar_4 == 0  and jaar_400 == 0:
    dag = 29
elif dag == 28 and maand == 2 and jaar_4 == 0 and not jaar_100 == 0 :
    dag = 29
elif dag == 28 and maand == 2:
    dag = 1
    maand += 1
else:
    dag += 1

#uitvoer

print(str(dag) + '/' + str(maand) + '/' + str(jaar))
