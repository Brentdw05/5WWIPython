

def is_letter(een_teken):
    if ord(een_teken) >= ord('A') <= ord('Z') or ord(een_teken) >= ord('a') <= ord('z'):
        return True
    else:
        return False


def roteer_letter(een_letter, caesarcijfer):
    nieuwe_letter = ""
    nieuwe_letter += chr(ord(een_letter)+ caesarcijfer)
    return nieuwe_letter


def versleutel(tekst, caesarcijfer):
    tekst_einde = ''
    for letter in range(tekst):
     tekst_einde += roteer_letter(letter, caesarcijfer)


print(versleutel('Het leven bestaat voor 10% uit dingen die gebeuren en voor 90% uit hoe jij daarop reageert.', 20))



