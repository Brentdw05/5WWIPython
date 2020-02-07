
def verwijder_medeklinkers(woord):
    nieuw_woord = ''
    for i in range(len(woord)):
        if woord[i] == 'z'or woord[i] == 'r'or woord[i] == 't'or woord[i] == 'p'or woord[i] == 'q'or woord[i] == 's'or woord[i] == 'd'or woord[i] == 'f'or woord[i] == 'g'or woord[i] == 'h'or woord[i] == 'k'or woord[i] == 'l'or woord[i] == 'm'or woord[i] == 'w'or woord[i] == 'x'or woord[i] == 'c'or woord[i] == 'v'or woord[i] == 'b'or woord[i] == 'n':
            while woord[i] != 'a'or woord[i] != 'e' or woord[i] != i or woord[i] != 'u':

        else:
            nieuw_woord += woord[i]
    return nieuw_woord



print(verwijder_medeklinkers('schil'))



#def varkenslatijn(woord):
#    nieuw_woord = ''
#   for i in range(len(woord)):
#       if i == 1 and woord[i] == 'a' or woord[i] == 'e' or woord[i] == 'i' or woord[i] == 'o' or woord[i] == 'u':
#           nieuw_woord += woord[:len(woord)] + 'ibus'
#       elif i == len(woord) and woord[i] == 'a' or woord[i] == 'i' or woord[i] == 'u':
#           nieuw_woord += woord + 'nt'
#        elif woord[i] == 'z'or woord[i] == 'r'or woord[i] == 't'or woord[i] == 'p'or woord[i] == 'q'or woord[i] == 's'or woord[i] == 'd'or woord[i] == 'f'or woord[i] == 'g'or woord[i] == 'h'or woord[i] == 'k'or woord[i] == 'l'or woord[i] == 'm'or woord[i] == 'w'or woord[i] == 'x'or woord[i] == 'c'or woord[i] == 'v'or woord[i] == 'b'or woord[i] == 'n':
#              while woord[i] != 'a' or woord[i] != 'e' or woord[i] != 'i' or woord[i] != 'o'or woord[i] != 'u':
#               nieuw_woord += verwijder_medeklinkers(woord) + 'itum'

#   return nieuw_woord



#print(varkenslatijn('icarus'))





