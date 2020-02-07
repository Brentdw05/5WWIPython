
def roteer(woord, n):
    geroteerd_woord = ''
    for letter in woord:
        x = woord.find(letter) + n
        if x >= len(woord)-1:
            while x >= len(woord)-1:
                x -= len(woord)
        else:
            pass
        geroteerd_woord += woord[x]
    return geroteerd_woord



print(roteer('asimov', 1))
