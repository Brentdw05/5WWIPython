

def germaniseer(tekst):
    #--> werk met nieuwe zin += . . .
    nieuwe_zin = ''
    # overloop alle letters van de string
    for i in range(0, len(tekst)):
        #indien de letter een spatie is
        if tekst[i] == ' ':
            #volgende letter wordt een hoofdletter
            nieuwe_zin +=' ' + tekst[i + 1].upper()
        elif i == 0:
            #eerste letter moet ook een hoofdletter zijn
            nieuwe_zin += tekst[i].upper()
        elif tekst[i-1] == ' ':
            pass
        else:
            nieuwe_zin += tekst[i]
    return nieuwe_zin


print(germaniseer('dit is een test'))
