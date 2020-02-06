

def ontdubbelen(woord):
    for i in range(len(woord)):
        if woord[i] == woord[i-1]:
            woord -= woord[:i-1] + '' + woord[i:]
    return woord



print(ontdubbelen('aaien'))




