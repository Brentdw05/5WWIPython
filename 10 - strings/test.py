
woord = input('geef woord: ')



#for i in range(-len(woord), 0):
#    print(woord[i])
#= for letter in woord:
#   print(letter)


for i in range (0, len(woord)):
    if woord[i] in 'aeoui':
        woord = woord[:i] + '*' + woord[i + 1:]


print(woord)
