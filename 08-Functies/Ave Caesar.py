

def is_letter(een_teken):
    if ord(een_teken) >= ord('A') <= ord('Z') or ord(een_teken) >= ord('a') <= ord('z'):
        return True
    else:
        return False


def roteer_letter(een_letter, Caesarcijfer):
    return chr(ord(een_letter) + caesarcijfer)


def versleutel(tekst, caesarcijfer):
    nieuwe_tekst = ''

        nieuwe_tekst += chr(letter + caesarcijfer)


print(versleutel('Het leven bestaat voor 10% uit dingen die gebeuren en voor 90% uit hoe jij daarop reageert.', 20))



