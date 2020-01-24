

def is_letter(een_teken):
    if ord(een_teken) >= ord('A') <= ord('Z') or ord(een_teken) >= ord('a') <= ord('z'):
        return True
    else:
        return False


def roteer_letter(letter, caesarcijfer):
    volgnummer_letter = min(ord(letter) % ord('a'), ord(letter) % ord('A'))
    nieuw_volgnummer = (volgnummer_letter + caesarcijfer) % 26
    offset = nieuw_volgnummer - volgnummer_letter
    return chr(ord(letter) + offset)


def versleutel(tekst, caesarcijfer):
    rotatie = ''
    for letter in tekst:
        rotatie += roteer_letter(letter, caesarcijfer)
    return rotatie



