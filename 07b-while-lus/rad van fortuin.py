
woord = input('geef woord: ')

bedrag = int(input('geef getal: '))

letter = input('geef letter: ')

gegokte_letter = ""

geldsom = 0

while letter in woord and not letter in gegokte_letter:
    gegokte_letter += letter
    geldsom += bedrag
    letter = input('letter: ')

print(geldsom)
