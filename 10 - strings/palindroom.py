

def is_palindroom(woord):
    omgekeerd = woord[::-1]
    if omgekeerd == woord:
        return True
    else:
        return False



print(is_palindroom('aa'))
